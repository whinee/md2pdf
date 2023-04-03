import base64
import os
import shutil
from datetime import date

from .cfg import rcfg
from .utils import vls_str

# Constants
ICONS = ["issues", "forks", "stars", "contributors", "license", "code"]
LANGS = ["python", "html", "yaml"]
OS = ["linux", "win"]

OP_CHOLDER_TPL = """by [{cholder}, Github account <a target=_blank
href="https://github.com/{user}">{user}</a> owner, {year}] as part of project
<a target=_blank href="https://github.com/{org}/{project}">{project}</a>"""

M_CHOLDER_TPL = """Copyright for portions of project <a target=_blank
href="https://github.com/{org}/{project}">{project}</a> are held {mc}.

All other copyright for project <a target=_blank
href="https://github.com/{org}/{project}">{project}</a> are held by [Github
Account <a target=_blank href="https://github.com/{user}">{user}</a> Owner, {year}]."""

S_CHOLDER_TPL = """Copyright (c) {year} Github Account <a target=_blank
href="https://github.com/{user}">{user}<a> Owner"""

# Derived Constants
VYML = rcfg("version.yml")
YML = rcfg("dev/vars.yml")

VLS = VYML["ls"]
LICENSE = YML["license"]
MD_VARS = YML["md_vars"]

VER_DIR = ["dev", "constants", "version", *[str(_) for _ in VLS[0:2]]]
GLOBAL = MD_VARS["global"]

PN = GLOBAL["project_name"]
ORG = GLOBAL["organization"]
USER = GLOBAL["user"]

# Initialize
cholder_ls = []


# Functions
def b64(name: str) -> str:
    with open(f"./docs/assets/images/icons/{name}", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def vrcfg(file: str):
    return rcfg(os.path.join(*VER_DIR, f"{file}.yml"))


def init() -> None:
    if os.path.isdir("docs"):
        shutil.rmtree("docs")
        os.makedirs("docs")
    shutil.copytree("dev/raw_docs/assets/", "docs/assets/")


if LICENSE["cholder"]:
    for c, mp in LICENSE["cholder"].items():
        user = mp.get("user", c)
        for org, projects in mp["projects"].items():
            for project, pm in projects.items():
                cholder_ls.append(
                    OP_CHOLDER_TPL.format(
                        cholder=c,
                        org=org,
                        project=project,
                        user=user,
                        year=pm["year"],
                    ),
                )
    if len(cholder_ls) > 1:
        cholder_ls[-2] += f", and {cholder_ls[-1]}"
        del cholder_ls[-1]
    cholder = M_CHOLDER_TPL.format(
        mc=", ".join(cholder_ls),
        org=ORG,
        project=PN,
        user=USER,
        year=LICENSE["year"],
    )
else:
    cholder = S_CHOLDER_TPL.format(user=USER, year=LICENSE["year"])


global_append = {
    "year": str(date.today().year),
    "cholder": cholder,
}

for k, v in zip(["vls", "ver", "sver"], [VLS, *vls_str(VLS)]):
    global_append[k] = v

for idx, i in enumerate(["user", "dev", "minor", "patch", "pri", "prv"]):
    global_append[f"ver_{i}"] = str(VLS[idx])

for i in ICONS:
    global_append[f"{i}_b64"] = b64(f"{i}.png")

for k, v in vrcfg("lang/en").dir("text/common/info").items():
    global_append[k] = v["str"]

MD_VARS["global"] = {
    **GLOBAL,
    **global_append,
}

RMDV = {"rules": YML["rules"], "md_vars": MD_VARS}
