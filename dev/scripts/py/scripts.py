import itertools
import re
from typing import Any

from .cfg import dcfg, pcfg, rcfg
from .md_vars import MD_VARS
from .utils import inmd

# Initialize Variables
MATRIX = {}
GLOBAL = {}
LOCAL = {}

# Constants
RE_MX = r"(?<=\{matrix.)[a-zA-Z0-9-_]+?(?=\})"

# Derived Constants
VYML = rcfg("version.yml")

VLS = VYML["ls"]

VER_DIR = f"dev/constants/version/{VLS[0]}/{VLS[1]}"

SCRIPTS = rcfg(f"{VER_DIR}/scripts/meta.yml")

with open("requirements.txt") as f:
    REQ = f.read().split("\n")

PG = {
    "prerel": not (VLS[-2] == 3),
    "ver_dir": VER_DIR,
    **{"ver_" + k: v for k, v in zip(["u", "d", "m", "p", "pi", "pv"], VLS)},
}

PL: dict[str, str] = {}

for k, v in SCRIPTS["matrix"].items():
    MATRIX[k] = [str(i) for i in v]

for k, v in dict(MD_VARS["global"], **SCRIPTS["variables"]["global"], **PG).items():
    GLOBAL[k] = str(v)

for k, v in dict(MD_VARS["local"], **SCRIPTS["variables"]["local"]).items():
    LOCAL[k] = str(v)


def cd(*k: list[str]) -> list[Any]:
    op = []
    dls = [MATRIX[i] for i in k]
    for i in itertools.product(*dls):
        op.append(dict(zip(k, i)))
    return op


def repl(key: str, path: str, op_path: str) -> tuple[str, str]:
    lv = SCRIPTS.dir(f"variables/local/{key}", {})
    rmvg = {**GLOBAL, **lv}

    for k, v in rmvg.items():
        path = path.replace("{{" + k + "}}", v)
        op_path = op_path.replace("{{" + k + "}}", v)

    with open(path) as f:
        contents = f.read()

    for k, v in rmvg.items():
        contents = contents.replace("{{" + k + "}}", v)

    return op_path, contents


def mr(k: str, v: dict[str, str]) -> list[list[str]]:
    path, contents = repl(k, v["path"], v["op_path"])
    if mx_match := re.findall(RE_MX, path):
        op = []
        for i in cd(*mx_match):
            _path = path.copy()
            _contents = contents.copy()
            for k, v in i.items():
                _path = _path.replace("{{matrix." + k + "}}", v)
                _contents = _contents.replace("{{matrix." + k + "}}", v)
            op.append([_path, _contents])
        return op
    else:
        return [[path, contents]]


def main() -> None:
    for k, v in SCRIPTS["scripts"].items():
        for path, contents in mr(k, v):
            with open(inmd(path), "w") as f:
                if og_ext := v.get("og_ext"):
                    if ext := v.get("ext"):
                        contents = dcfg(pcfg(contents, og_ext), ext)
                f.write(contents)
