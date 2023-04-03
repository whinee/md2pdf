import re
from functools import partial
from os import path
from pathlib import Path
from typing import Any, Optional, TypeAlias, Union

import inquirer

from .cd import CustomDict
from .cfg import rcfg, wcfg
from .md_vars import RMDV, VYML, vrcfg
from .schema import Config
from .utils import run, vls_str

# Constants
VERSIONS_NAME = [
    "User",
    "Dev",
    "Minor",
    "Patch",
    "Pre-release identifier",
    "Pre-release version",
]
DE_PUSH_MSG = "For info, check `docs/latest-commit.md` or this commit's comments"
PUSH_CMD = 'git commit -am "{}"'
RE_MOD_DS = r"(def {}\(.*?:\s*?\n(\s+)(([\'\"])\4\4)).+?(?=\s*(?:Args:|Returns:|Raises:|Yields:|\3))"

# First Dependents
VLS = VYML["ls"]
VER_DIR = ["dev", "constants", "version", *[str(_) for _ in VLS[0:2]]]


# Derived Constants
VLS_STR_RE = re.compile(r"^(((0|[1-9][0-9]*) ){4}([0-2] (0|[1-9][0-9]*)|3 0))$")
PROJECT_CFG = vrcfg("project")
INIT_FILE = PROJECT_CFG["init_file"]
GLOBAL = RMDV["md_vars"]["global"]

# Types
DOD_TYPE: TypeAlias = str | dict[str, Union[str, "DOD_TYPE"]]


# Modules
def scripts_mod(*args, **kwargs) -> None:
    from .scripts import main

    main(*args, **kwargs)


def docs_mod(*args, **kwargs) -> None:
    from .docs import main

    main(*args, **kwargs)


# Functions
def _mod_ds(desc, match):
    indent = match.group(2)
    fl, *op = desc.strip().split("\n")
    return match.group(1) + "\n".join([fl, *[indent + i if i else i for i in op]])


def mod_ds(script: str, function: str, desc: str):
    with open(script) as f:
        ip = f.read()

    op = re.sub(
        RE_MOD_DS.format(function),
        partial(_mod_ds, desc),
        ip,
        0,
        re.MULTILINE,
    )

    with open(script, "w") as f:
        f.write(op)


def mod_ds_cfg(script: Optional[str], function: Optional[str], dod: DOD_TYPE) -> None:
    if isinstance(dod, dict):
        if isinstance(script, str) and isinstance(function, str):
            script += "/" + function
        elif isinstance(function, str):
            script = function
        for k, v in dod.items():
            mod_ds_cfg(script, k, v)
    elif isinstance(script, str) and isinstance(function, str) and isinstance(dod, str):
        mod_ds(script + ".py", function, dod)
    else:
        if not (isinstance(dod, dict) or isinstance(dod, str)):
            raise TypeError(f"Type {type(dod)} not allowed.")


def cc() -> None:
    const_dir = PROJECT_CFG["const_dir"]
    lang_path = PROJECT_CFG["lang_dir"].format(const_dir=const_dir)

    for k, v in PROJECT_CFG["cp"].items():
        wcfg(f'{v["dir"].format(const_dir=const_dir)}.{v.get("ext", "mp")}', vrcfg(k))

    cf_tpl = vrcfg("config")
    Config(cf_tpl["version"])(cf_tpl["config"], const_dir)

    for i in list(Path(path.join(*VER_DIR, "lang")).rglob("*[!.test].yml")):
        tl_yml = CustomDict()

        for k, v in rcfg(i)["text"].items():
            for vk, vv in v.items():
                for vvk, vvv in vv.items():
                    tl_yml.modify("/".join([k, vk, vvk]), vvv["str"])

        wcfg(path.join(lang_path, path.splitext(path.basename(i))[0] + ".mp"), tl_yml)

    wcfg(const_dir + "/const.mp", {k: v for k, v in GLOBAL.items() if "b64" not in k})
    if ds_cfg := PROJECT_CFG.get("docstrings", None):
        mod_ds_cfg(None, None, ds_cfg)


def docs() -> None:
    cc()
    scripts_mod()

    docs_mod(RMDV)


def push(v: Optional[list[int]] = None) -> None:
    """
    Push changes to the remote repository. Pass version list of numbers to add.

    Args:
    - v (`list[int]`, optional): _description_. Defaults to `None`.
    """
    msg = inquirer.text(message="Enter commit message", default="")

    docs()
    run("just lint")
    run("git add .")

    if msg == "":
        msg = DE_PUSH_MSG
    else:
        msg = "\n" + msg

    if v:
        msg = "\n".join(
            [
                "VERSION BUMP: ",
                msg,
                f"Release notes: https://{GLOBAL['site']}/changelog#{'-'.join([str(i) for i in v])} or `docs/latest release notes.md`",
            ],
        )

    run(PUSH_CMD.format(msg))
    run("git push")


def dcomp(x: int) -> list[int]:
    """
    Given a number x, return a list of times a prime factor of x occured.

    Args:
        x (int): Number to get the prime factors of.

    Returns:
        list[int]: List of times a prime factor of x occured.
    """
    primes = [3, 2]
    factors = [0 for _ in primes]
    while x != 1:
        for idx, i in enumerate(primes):
            if x % i == 0:
                factors[idx] += 1
                x = int(x / i)
                break
            else:
                pass
    return factors


def _set_ver(vls: list[int]) -> None:
    """
    Set version, and write to file.

    Args:
        vls (list[int]): Version list.
    """
    const_path = PROJECT_CFG["const_dir"] + "/const.mp"
    const_mp = rcfg(const_path)
    op_ls = [vls, *vls_str(vls)]

    wcfg("version.yml", dict(zip(["ls", "str", "sv"], op_ls)))
    for k, v in zip(["vls", "__version__", "hver"], op_ls):
        const_mp[k] = v
    wcfg(const_path, const_mp)


def vfn(answers: list[Any], current: str) -> bool:
    """
    Validation Function for version bump prompt. Check if given string to the prompt matches the regex for version.

    Args:
    - answers (`list[Any]`): Unused, list of answers from the previous prompts.
    - current (`str`): Current answer to the prompt.

    Raises:
    - `Exception`: If the given string to the prompt does not match the regex for version.

    Returns:
    `bool`: True, if the given string to the prompt matches the regex for version.
    """

    match = VLS_STR_RE.match(current)
    if match is None:
        raise Exception("Invalid version digits")

    x, y = match.span()
    vls = current[x:y].strip().split(" ")
    if len(vls) != 6:
        raise Exception("Invalid version digits")

    _set_ver([int(i) for i in vls])
    return True


def vlir(idx: int, vls: list[int]) -> list[int]:
    """
    Version Lower than Index will be Reset.

    Args:
        idx (int): Index to compare to.
        vls (list[int], optional): Version list.

    Returns:
        list[int]: Modified version list.
    """

    for i in range(idx + 1, len(vls)):
        if i == 4:
            vls[i] = 3
        else:
            vls[i] = 0
    return vls


def _bump(idx: int) -> list[int]:
    """
    Bump's inner function. Given the index of the version part to bump, bump the said part and output that.

    Args:
        idx (int): Index to bump.

    Returns:
        list[int]: Modified version list.
    """

    _vls = list(VLS)
    if idx == 4:
        if _vls[idx] == 3:
            _vls[3] += 1
            _vls[4] = _vls[5] = 0
        else:
            _vls = vlir(idx, _vls)
            _vls[idx] += 1
    else:
        _vls = vlir(idx, _vls)
        _vls[idx] += 1
    return _vls


def bump() -> None:
    """Bump program's version."""
    while True:
        choices = []
        for idx, k in enumerate(VERSIONS_NAME):
            choices.append([f"{k.ljust(23)}(bump to {vls_str(_bump(idx))[0]})", idx])
        idx = inquirer.list_input(
            message=f"What version do you want to bump? (Current version: {vls_str(VLS)[0]})",
            choices=choices,
        )
        _vls = _bump(idx)
        print(
            f"    This will bump the version from {vls_str(VLS)[0]} to {vls_str(_vls)[0]} ({VERSIONS_NAME[idx]} bump). ",
        )
        match inquirer.list_input(
            message="Are you sure?",
            choices=[
                ["Yes", "y"],
                ["No", "n"],
                ["Cancel", "c"],
            ],
        ):
            case "y":
                _set_ver(_vls)
                push(_vls)
                return
            case "n":
                continue
            case "c":
                break
            case _:
                pass


def main(choice: str) -> None:
    """
    Main function.

    Args:
    - choice (`str`): Subcommand to run.
    """
    match choice:
        case "ver":
            for k, v in zip(
                ["Version       ", "Semver Version"],
                vls_str(VLS),
                strict=True,
            ):
                print(f"{k}: {v}")
        case "cc":
            cc()
        case "docs":
            docs()
        case "push":
            push()
        case "gs":
            scripts_mod()
        case "bump":
            bump()
        case "set_ver":
            inquirer.text(
                message="Enter version digits seperated by spaces",
                validate=vfn,
            )
        case _:
            print(f"menu: {choice} is not in the menu.")
