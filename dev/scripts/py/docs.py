import json
import os
import re
import shutil
from functools import partial
from io import StringIO
from os import listdir
from os.path import dirname as dn
from pathlib import Path
from typing import Any, Dict, List, Optional

import frontmatter
import panflute
import pdoc
import pypandoc
import yaml
from mako.template import Template

from .md_vars import VYML, YML
from .utils import cycle_2ls, inmd, noop, repl, run

# Constants
HA_VNS = 2
HA_VNE = 11

MD_HEADER = """
<style>
ul{
  padding-left: 20px;
}
</style>
"""

AW = '<a href="#{id}">{content}</a>'
HW = '<h{n} id="{id}">{title}</h{n}>\n'
HA_RSTYLE = ["<b>{}</b>", "<b><i>{}</i></b>", "{}", "<i>{}</i>"]
H1 = '<h1 align="center" style="font-weight: bold">\n    {}\n</h1>\n\n'
H1_MD = H1 + "{}\n"
H1_LINK_MD = H1.format('<a target="_blank" href="{}">{}</a>') + "{}\n"

# Constants
RE_MDSE = r"(?<=# {key} start\n).+(?=\n\s*# {key} end)"

INFO_TPLS = {
    "site_name": [None, ["project_name"]],
    "site_url": ["https://{}", ["site"]],
    "repo_url": ["https://github.com/{}/{}", ["organization", "repo_name"]],
    "site_description": [None, ["long_desc"]],
    "site_author": [None, ["author"]],
    "copyright": ["Copyright &copy; {} {}", ["year", "author"]],
}

# Derived Constants
VLS = VYML["ls"]

PDOC = YML["pdoc"]
MAKO = YML["mako"]
DOCS = YML["docs"]

IDF = Path(DOCS["input"])

HTI_RF = re.compile(r"[\s\d\w]+", re.MULTILINE | re.DOTALL | re.UNICODE).findall
TOMD_RS = partial(re.compile("-{2,}").sub, "-")

CONTEXT = pdoc.Context()
PROJECT = pdoc.Module(PDOC["project"], context=CONTEXT)
pdoc.link_inheritance(CONTEXT)
pdoc.tpl_lookup = pdoc.TemplateLookup(directories=[PDOC["tpl"]])

H1_STYLE = HA_RSTYLE[0]


# Variable Initialization
HA_STYLE = {}


# Class Initialization
class Constants:
    pass


# Function Initialization
def str_presenter(dumper, data: str):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


# Last Initialization
TOC_H2A = H1_STYLE.format(AW.format(id="toc", content="Table of Contents"))
TOC_H2 = HW.format(n=2, id="toc", title=TOC_H2A)
hs = HA_VNS - 1
for i, j in cycle_2ls(range(HA_VNS, HA_VNE + 1), HA_RSTYLE):
    if j == H1_STYLE:
        hs += 1
    HA_STYLE[i] = [hs, j]
# pprint(HA_STYLE)


yaml.add_representer(str, str_presenter)


# Functions
def _sh_inner(toc_ls, res_ls, elem, iid) -> None:
    op = []
    for i in elem.content.walk(noop):
        if isinstance(i, panflute.Str):
            op.append(i.text)

    level, fs = HA_STYLE[elem.level]
    t = " ".join(op)
    a = AW.format(id=iid, content=t)
    toc_ls.append(f'{"    " * (elem.level - 2)}- {a}')
    elem.identifier = ""
    res_ls.append(
        [
            pfelem2md(elem, elem.doc),
            HW.format(n=level, id=iid, title=fs.format(a)),
        ]
    )


def dd(
    od: Dict[str, List[str]], *dicts: List[Dict[str, List[str]]]
) -> Dict[str, List[str]]:
    for d in dicts:
        for a, v in d.items():
            od[a] = [*(od.get(a, []) or []), *v]
    return od


def docs_dir(mn: str, absolute: bool = True, api=False) -> str:
    mls = mn.split(".")
    if (len(mls) == 1) and (PDOC["project"] == mls[0]):
        mls[0] = "index"
    elif (len(mls) >= 2) and (PDOC["project"] == mls[0]):
        del mls[0]
    rel_ls = [*[str(i) for i in VLS[0:2]], *mls[:-1], f"{mls[-1]}.md"]
    if api:
        rel_ls.insert(2, "api")
        rel_ls.insert(0, "docs")
    rel = os.path.join(*rel_ls)
    abs = os.path.join(PDOC["op"], rel)
    inmd(abs)
    if absolute:
        return abs
    else:
        return rel


def elem_str(elem) -> str:
    op = []
    for i in elem.walk(noop):
        if isinstance(i, panflute.Str):
            op.append(i.text)
    return " ".join(op)


def get_header_id(h: panflute.Header) -> str:
    return TOMD_RS("-".join(HTI_RF(elem_str(h).lower().strip())).replace(" ", "-"))


def pf_set_element():
    ld = -1

    def inner(d: list[Any], lvl: int, elem, og_lvl: Optional[int] = None):
        global ld
        if og_lvl is None:
            og_lvl = lvl
        if lvl == 0:
            d.append(elem)
            ld = og_lvl
        elif og_lvl != -1:
            e = d[-1]
            if not isinstance(d[-1], list):
                d[-1] = ["d2hpX25lJ3Mgc2VjcmV0OiBrdg==", e, []]
            inner(d[-1][-1], lvl - 1, elem, og_lvl)

    return inner


def pfelem2md(elem, doc):
    return pypandoc.convert_text(
        json.dumps(
            {
                "pandoc-api-version": doc.to_json()["pandoc-api-version"],
                "meta": {},
                "blocks": [elem.to_json()],
            }
        ),
        to="md",
        format="json",
    )


def rules_fn(rules: Dict[Any, Any]) -> Dict[str, List[str]]:
    return dd({"": rules.get("del", [])}, rules["repl"])


def style_header(toc_ls, res_ls):
    _si = partial(_sh_inner, toc_ls, res_ls)

    def inner(item, parent=None):
        id_ls = []
        if parent is not None:
            id_ls = [parent]
        if not isinstance(item, list):
            _si(item, "-".join(id_ls + [get_header_id(item.content)]))
        else:
            if len(item) >= 1:
                k = item.pop(0)
                if k == "d2hpX25lJ3Mgc2VjcmV0OiBrdg==":
                    k, v = item
                    id_ls += [get_header_id(k.content)]
                    iid = "-".join(id_ls)
                    _si(k, iid)
                    for i in v:
                        inner(i, iid)
                else:
                    for i in [k] + item:
                        inner(i, "-".join(id_ls) if id_ls else None)

    return inner


def style_header_init(hls, se, lower_than_four):
    def inner(elem, doc):
        if isinstance(elem, panflute.Header):
            se(hls, elem.level - 2, elem)

    return inner


def yield_text(mod):
    yield mod.name, mod.text()
    sm = {}
    for submod in mod.submodules():
        sm[submod.name] = docs_dir(submod.name, api=True)
        yield from yield_text(submod)

    if sm:
        header = []
        idx_path = docs_dir(mod.name, api=True)
        m, *ls = mod.name.split(".")
        for idx, i in enumerate(ls[::-1]):
            header.append(f'[{i}]({"../" * idx}{i}.md)')
        header = ".".join(
            [f"[{m}](" + "../" * (len(ls) - 1) + "index.md)"] + header[::-1]
        )

        if sum := mod.supermodule:
            docs_dir(sum.name, api=True)
            sum = f'\n\n## **<a href="#super" id="super">Super-module</a>**\n- [{sum.name}](index.md)\n'
        else:
            sum = ""

        smls = []
        for k, v in sm.items():
            v = "/".join(v.split("/")[5:])
            smls.append(f"- [{k}]({v})")
        sm = '\n\n## **<a href="#sub" id="sub">Sub-modules</a>**\n\n{}\n'.format(
            "\n".join(smls)
        )

        idx = """# **{}**{}{}""".format(
            header,
            sum,
            sm,
        )

        with open(idx_path, "w") as f:
            f.write(idx)


def main(rmv: Dict[Any, Any] = {}):
    docs_pdir = DOCS["op"]
    rmv_r = rmv["rules"]
    rmv_mv = rmv["md_vars"]
    rmv_mv_g = rmv_mv["global"]

    # del_gen()

    for rip in list(IDF.rglob("*.ymd")):
        fm = {}
        hls = []
        toc_ls = []
        res_ls = []
        tp = False

        out = os.path.join(docs_pdir, *rip.parts[2:-1], f"{rip.stem}.md")

        print(f"Generating {out}")

        rf = frontmatter.load(rip)
        md = repl(rf.content, rules_fn(rmv_r))
        md_data = pypandoc.convert_text(md, "json", format="md")
        d = dict(
            rmv_mv_g,
            **rmv_mv.dir(f"local/{rip.stem}", {}),
        )

        if title := rf.get("title"):
            fm["title"] = title
            if link := rf.get("link"):
                md = H1_LINK_MD.format(link, title, md)
            else:
                md = H1_MD.format(title, md)

        for k, v in d.items():
            md = md.replace("{{" + k + "}}", str(v))

        panflute.run_filter(
            style_header_init(hls, pf_set_element(), "####" in md),
            doc=panflute.load(StringIO(md_data)),
        )
        style_header(toc_ls, res_ls)(hls)

        for k, v in res_ls:
            if not tp:
                toc_html = pypandoc.convert_text("\n".join(toc_ls), "html", format="md")
                toc_html = toc_html.replace(">\n<", "><").strip().replace("\n", " ")
                v = '\n<div class="toc">' + TOC_H2 + toc_html + "</div>\n\n" + v
                tp = True
            md = md.replace(k, v, 1)

        with open(inmd(out), "w") as f:
            f.write(md)

    for module_name, yt in yield_text(PROJECT):
        _dd = docs_dir(module_name, api=True)
        with open(_dd, "w") as f:
            f.write(yt)

    makos = []

    for g in MAKO["gen"]["glob"]:
        for i in list(Path(".").rglob(g)):
            makos.append(str(i))

    for i in MAKO["gen"]["path"]:
        ip = os.path.join(DOCS["input"], i)
        if os.path.isfile(ip):
            makos.append(ip)
        else:
            print(f"{ip} not found")

    for ip in makos:
        pip = Path(ip)
        stem = "README" if pip.stem == "index" else pip.stem
        op = os.path.join(docs_pdir, *pip.parts[2:-1], f"{stem}.md")
        mytemplate = Template(filename=ip)
        tpl_rd = mytemplate.render(
            **{
                "cwd": dn(ip),
            }
        )
        with open(op, "w") as f:
            f.write(tpl_rd)

    op_base = "docs"
    base = "dev/raw_docs/docs"

    ndd = {}
    u_ls = sorted(listdir(base), reverse=True)
    with open(os.path.join(docs_pdir, op_base, "README.md"), "w") as f:
        print("here")
        f.write(
            H1.format("All Version")
            + "\n".join(f"- [Version {u}.x.x.x]({u}/README.md)" for u in u_ls)
        )
    for u in u_ls:
        d_ls = sorted(listdir(os.path.join(base, u)), reverse=True)
        with open(
            os.path.join(os.path.join(docs_pdir, op_base, u), "README.md"), "w"
        ) as f:
            f.write(
                H1.format(f"Version {u}.x.x.x")
                + "\n".join(f"- [Version {u}.{d}.x.x]({d}/README.md)" for d in d_ls)
            )
        for d in d_ls:
            ndd[f"{u}.{d}"] = os.path.join(op_base, u, d)

    lk = list(ndd.keys())[-1]
    ndd[f"{lk} (Current)"] = ndd.pop(lk)

    new_ndd = {}
    for k, v in reversed(ndd.items()):
        new_ndd[k] = v
    nd = yaml.dump(new_ndd, default_flow_style=False)

    nd = "\n".join([f"    - {i}" for i in nd.strip().split("\n")][::-1])

    with open("mkdocs.yml", "r") as f:
        mkdocs = f.read()

    info_yml = {}
    for k, (f, kls) in INFO_TPLS.items():
        vd = {i: rmv_mv_g.get(i, None) for i in kls}
        if f is None:
            op = " ".join([str(i) for i in vd.values()])
        else:
            op = f.format(*vd.values(), **vd)
        info_yml[k] = op
    mkdocs = re.sub(
        RE_MDSE.format(key="info"),
        yaml.dump(info_yml, indent=2, sort_keys=False),
        mkdocs,
        0,
        re.S,
    )

    with open("mkdocs.yml", "w") as f:
        f.write(re.sub(RE_MDSE.format(key="nav docs"), nd, mkdocs, 0, re.S))
    shutil.copy("mkdocs.yml", "mkdocs.bak.yml")

    run("mkdocs build")
