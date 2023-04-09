import json
import os
import re
import shutil
from collections.abc import Callable, Generator
from functools import partial
from io import StringIO
from os import listdir
from os.path import dirname as dn
from pathlib import Path
from typing import Any, Optional

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

AW = '<a href="#{id}">{content}</a>'  # A tag
HW = '<h{n} id="{id}">{title}</h{n}>\n'
HA_DEF_STYLE = "<b>{}</b>"  # Header All Default Style
HA_RSTYLE = [
    HA_DEF_STYLE,
    "<b><i>{}</i></b>",
    "{}",
    "<i>{}</i>",
]  # Header All Repeated Style
H1 = '<h1 align="center" style="font-weight: bold">\n    {}\n</h1>\n\n'
H1_MD = H1 + "{}\n"
H1_LINK_MD = H1.format('<a target="_blank" href="{}">{}</a>') + "{}\n"
SMH = '\n\n## **<a href="#sub" id="sub">Sub-modules</a>**\n\n{}\n'  # sub-module heading

RE_MDSE_FMT = r"(?<=# \[DO NOT MODIFY\] {key} start\n).+(?=\n\s*# {key} end)"

INFO_TPLS: dict[str, tuple[None, list[str]] | tuple[str, list[str]]] = {
    "site_name": (None, ["project_name"]),
    "site_url": ("https://{}", ["site"]),
    "repo_url": ("https://github.com/{}/{}", ["organization", "repo_name"]),
    "site_description": (None, ["long_desc"]),
    "site_author": (None, ["author"]),
    "copyright": ("Copyright &copy; {} {}", ["year", "author"]),
}

# Derived Constants
H5_RE = re.compile(r"^#####", re.MULTILINE).search

VLS = VYML["ls"]

PDOC = YML["pdoc"]
MAKO = YML["mako"]
DOCS = YML["docs"]

DOCS_INPUT = DOCS["input"]  # Docs Input Directory
DOCS_IP_DOCS = os.path.join(DOCS_INPUT, DOCS["docs"])  # Docs Input Docs Directory
DOCS_OP = DOCS["op"]  # Docs Output Directory
DOCS_OP_TMP = DOCS["op_tmp"]  # Docs Temporary Output Directory
DOCS_OP_SITE = DOCS["op_site"]  # Docs Site Output Directory
DOCS_OP_DOCS = os.path.join(DOCS_OP, DOCS["docs"])  # Docs Outpot Docs Directory

MKDOCS_MOD_DOCS = {"docs_dir": DOCS_OP_TMP, "site_dir": DOCS_OP_SITE}
with open("mkdocs.yml") as f:
    MKDOCS_YML = f.read()

HTI_RF = re.compile(r"[\s\d\w]+", re.MULTILINE | re.DOTALL | re.UNICODE).findall
TOMD_RS = partial(re.compile("-{2,}").sub, "-")

CONTEXT = pdoc.Context()
PROJECT = pdoc.Module(PDOC["project"], context=CONTEXT)
pdoc.link_inheritance(CONTEXT)
pdoc.tpl_lookup = pdoc.TemplateLookup(directories=PDOC["tpl"])

H1_STYLE = HA_RSTYLE[0]

# Variable Initialization
HA_STYLE = {}


# Class Initialization
class Constants:
    pass


# Function Initialization
def str_presenter(dumper, data: str) -> Any:
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

ld = -1

yaml.add_representer(str, str_presenter)


# Functions
def mkdocs_mod(key: str, repl_str: str | list[Any] | dict[str, Any]) -> None:
    global MKDOCS_YML
    if not isinstance(repl_str, str):
        repl_str = yaml.dump(repl_str, indent=2, sort_keys=False).rstrip()
    MKDOCS_YML = re.sub(RE_MDSE_FMT.format(key=key), repl_str, MKDOCS_YML, 0, re.S)


def dd(
    od: dict[str, list[str]],
    *dicts: list[dict[str, list[str]]],
) -> dict[str, list[str]]:
    for d in dicts:
        if d is None:
            continue
        for a, v in d.items():
            od[a] = [*(od.get(a, []) or []), *v]
    return od


def pdoc_dir(mn: str) -> str:
    """mn: module name."""
    mls = mn.split(".")
    if (len(mls) == 1) and (PDOC["project"] == mls[0]):
        mls[0] = "index"
    elif (len(mls) >= 2) and (PDOC["project"] == mls[0]):
        del mls[0]

    abs = os.path.join(
        DOCS_OP_DOCS, *[str(i) for i in VLS[0:2]], "api", *mls[:-1], f"{mls[-1]}.md",
    )

    inmd(abs)

    return abs


def elem_str(elem: panflute.Inline) -> str:
    op = []
    for i in elem.walk(noop):
        if isinstance(i, panflute.Str):
            op.append(i.text)
    return " ".join(op)


def get_header_id(h: panflute.Header) -> str:
    return TOMD_RS("-".join(HTI_RF(elem_str(h).lower().strip())).replace(" ", "-"))


def pf_set_element() -> Callable[..., None]:
    def inner(d: list[Any], lvl: int, elem, og_lvl: Optional[int] = None) -> None:
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


def pfelem2md(elem, doc) -> str:
    return pypandoc.convert_text(
        json.dumps(
            {
                "pandoc-api-version": doc.to_json()["pandoc-api-version"],
                "meta": {},
                "blocks": [elem.to_json()],
            },
        ),
        to="md",
        format="json",
    )


def rules_fn(rules: dict[Any, Any]) -> dict[str, list[str]]:
    return dd({"": rules.get("del", [])}, rules["repl"])


def sh_ltf_inner(
    toc_ls: list[str], res_ls: list[list[str]], elem: panflute.Header, iid: str,
) -> None:
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
        ],
    )


def sh_inner(
    toc_ls: list[str], res_ls: list[list[str]], elem: panflute.Header, iid: str,
) -> None:
    op = []
    for i in elem.content.walk(noop):
        if isinstance(i, panflute.Str):
            op.append(i.text)

    level = elem.level
    t = " ".join(op)
    a = AW.format(id=iid, content=t)
    toc_ls.append(f'{"    " * (level - 2)}- {a}')
    elem.identifier = ""
    res_ls.append(
        [
            pfelem2md(elem, elem.doc),
            HW.format(n=level, id=iid, title=HA_DEF_STYLE.format(a)),
        ],
    )


def style_header(
    toc_ls: list[str], res_ls: list[list[str]], lower_than_four: bool,
) -> Callable[..., None]:
    if lower_than_four:
        _si = partial(sh_ltf_inner, toc_ls, res_ls)
    else:
        _si = partial(sh_inner, toc_ls, res_ls)

    def inner(item, parent=None):
        id_ls = []
        if parent is not None:
            id_ls = [parent]
        if not isinstance(item, list):
            _si(item, "-".join([*id_ls, get_header_id(item.content)]))
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
                    for i in [k, *item]:
                        inner(i, "-".join(id_ls) if id_ls else None)

    return inner


def style_header_init(hls, se) -> Callable[..., None]:
    def inner(elem: panflute.Element, doc: panflute.Doc) -> None:
        if isinstance(elem, panflute.Header):
            se(hls, elem.level - 2, elem)

    return inner


def yield_text(mod: pdoc.Module) -> Generator[Any, None, None]:
    yield mod.name, mod.text()
    sm = {}
    for submod in mod.submodules():
        sm[submod.name] = pdoc_dir(submod.name)
        yield from yield_text(submod)

    if not sm:
        return

    header_ls: list[str] = []
    idx_path = pdoc_dir(mod.name)

    print(f"Generating {idx_path}")

    m, *ls = mod.name.split(".")
    for idx, i in enumerate(ls[::-1]):
        header_ls.append(f'[{i}]({"../" * idx}{i}.md)')
    header = ".".join(
        [f"[{m}](" + "../" * (len(ls) - 1) + "index.md)"] + header_ls[::-1],
    )

    if sum := mod.supermodule:
        pdoc_dir(sum.name)
        sum = f'\n\n## **<a href="#super" id="super">Super-module</a>**\n- [{sum.name}](index.md)\n'
    else:
        sum = ""

    smls = []
    for k, v in sm.items():
        v = "/".join(v.split("/")[5:])
        smls.append(f"- [{k}]({v})")

    idx = """# **{}**{}{}""".format(
        header,
        sum,
        SMH.format("\n".join(smls)),
    )

    with open(idx_path, "w") as f:
        f.write(idx)


def ymd2md(
    rmv_rm: dict[str, dict[str, list[str]]],
    rmv_mv_g: dict[str, str],
    rmv_mv_l: dict[str, dict[str, str]],
    rip: Path,
) -> None:
    fm = {}
    hls: list[Any] = []
    toc_ls: list[str] = []
    res_ls: list[list[str]] = []
    tp = False

    out = os.path.join(DOCS_OP, *rip.parts[2:-1], f"{rip.stem}.md")

    print(f"Generating {out}")

    rf = frontmatter.load(rip)
    md = repl(rf.content, rules_fn(rmv_rm))
    md_data: str = pypandoc.convert_text(md, "json", format="md")
    d = dict(  # type: ignore[call-overload]
        rmv_mv_g,
        **rmv_mv_l.get(rip.stem, {}),
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
        style_header_init(hls, pf_set_element()),
        doc=panflute.load(StringIO(md_data)),
    )
    style_header(toc_ls, res_ls, bool(H5_RE))(hls)

    for k, v in res_ls:
        if not tp:
            toc_html = pypandoc.convert_text("\n".join(toc_ls), "html", format="md")
            toc_html = toc_html.replace(">\n<", "><").strip().replace("\n", " ")
            v = '\n<div class="toc">' + TOC_H2 + toc_html + "</div>\n\n" + v
            tp = True
        md = md.replace(k, v, 1)

    with open(inmd(out), "w") as f:
        f.write(md)


def src_docs() -> None:
    for module_name, yt in yield_text(PROJECT):
        _dd = pdoc_dir(module_name)
        print(f"Generating {_dd}")
        with open(_dd, "w") as f:
            f.write(yt)


def mako2md() -> None:
    # Initialize Variables
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
        op = os.path.join(DOCS_OP, *pip.parts[2:-1], f"{stem}.md")
        mytemplate = Template(filename=ip)
        tpl_rd = mytemplate.render(cwd=dn(ip))
        with open(op, "w") as f:
            f.write(tpl_rd)


def ver_docs() -> str:
    ndd = {}
    u_ls = sorted(listdir(DOCS_IP_DOCS), reverse=True)
    with open(os.path.join(DOCS_OP_DOCS, "README.md"), "w") as f:
        f.write(
            H1.format("All Version")
            + "\n".join(f"- [Version {u}.x.x.x]({u}/README.md)" for u in u_ls),
        )
    for u in u_ls:
        d_ls = sorted(listdir(os.path.join(DOCS_IP_DOCS, u)), reverse=True)
        with open(
            os.path.join(DOCS_OP_DOCS, u, "README.md"),
            "w",
        ) as f:
            f.write(
                H1.format(f"Version {u}.x.x.x")
                + "\n".join(f"- [Version {u}.{d}.x.x]({d}/README.md)" for d in d_ls),
            )

        for d in d_ls:
            with open(os.path.join(DOCS_IP_DOCS, u, d, "index.mmd")) as f:
                md_op = f.read()

            with open(os.path.join(DOCS_OP_DOCS, u, d, "README.md"), "w") as f:
                f.write(H1.format(f"Version {u}.{d}.x.x") + md_op)

            ndd[f"{u}.{d}"] = os.path.join(DOCS_OP, u, d)

    lk = list(ndd.keys())[-1]
    ndd[f"{lk} (Current)"] = ndd.pop(lk)

    nd = yaml.dump(dict(reversed(ndd.items())), default_flow_style=False)
    return "\n".join([f"    - {i}" for i in nd.strip().split("\n")][::-1])


def mkdocs_build(rmv_mv_g: dict[str, str], rmv_rs) -> None:
    info_yml = {}

    nd = ver_docs()

    for k, (f, kls) in INFO_TPLS.items():
        vd = {i: rmv_mv_g.get(i, None) for i in kls}
        if f is None:
            op = " ".join([str(i) for i in vd.values()])
        else:
            op = f.format(*vd.values(), **vd)
        info_yml[k] = op

    # Modify `mkdocs.yml`
    mkdocs_mod("info", info_yml)
    mkdocs_mod("dir", MKDOCS_MOD_DOCS)
    mkdocs_mod("nav docs", nd)

    with open("mkdocs.yml", "w") as f:
        f.write(MKDOCS_YML)
    shutil.copy("mkdocs.yml", "mkdocs.bak.yml")

    for dirpath, _, filenames in os.walk(DOCS_OP):
        for filename in filenames:
            input_path = os.path.join(dirpath, filename)
            with open(input_path) as f:
                contents = f.read()
                contents = repl(contents, rules_fn(rmv_rs))
                # Modify the contents of the file here

            # Create output directory if it doesn't exist
            output_subdir = os.path.join(DOCS_OP_TMP, os.path.relpath(dirpath, DOCS_OP))
            os.makedirs(output_subdir, exist_ok=True)

            output_path = os.path.join(output_subdir, filename)
            with open(output_path, "w") as f:
                f.write(contents)

    run("mkdocs build")

    shutil.rmtree(DOCS_OP_TMP)


def main(rmv: dict[Any, Any]) -> None:
    # Derived Constants
    rmv_r = rmv["rules"]
    rmv_mv = rmv["md_vars"]

    rmv_rm = rmv_r["md"]
    rmv_rs = rmv_r["site"]
    rmv_mv_g = rmv_mv["global"]
    rmv_mv_l = rmv_mv["local"]

    if os.path.isdir(DOCS_OP):
        shutil.rmtree(DOCS_OP)
    ymd2md_fn = partial(ymd2md, rmv_rm, rmv_mv_g, rmv_mv_l)
    for rip in list(Path(DOCS_INPUT).rglob("*.ymd")):
        ymd2md_fn(rip)
    src_docs()
    mako2md()
    if os.path.isdir(DOCS_OP_TMP):
        shutil.rmtree(DOCS_OP_TMP)
    shutil.copytree(
        os.path.join(DOCS_INPUT, "assets"), os.path.join(DOCS_OP_TMP, "assets"),
    )
    mkdocs_build(rmv_mv_g, rmv_rs)
    shutil.copytree(os.path.join(DOCS_INPUT, "assets"), os.path.join(DOCS_OP, "assets"))
