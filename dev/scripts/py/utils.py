import shlex
from collections.abc import Iterable, Sized
from itertools import cycle
from os import makedirs, path
from subprocess import call
from typing import Any, Optional

# Constants

PR = ["alpha", "beta", "rc"]


# Functions
def cycle_2ls(a: Sized, b: Sized) -> Iterable[Any]:
    op: Iterable[Any] = (
        zip(a, cycle(b), strict=False)
        if len(a) > len(b)
        else zip(cycle(a), b, strict=False)
    )
    return op


def dnn(fn: str, n: int) -> str:
    op = fn
    for _ in range(n):
        op = path.dirname(op)
    return op


def inmd(p: str, ls: Optional[list[str]] = None) -> str:
    """
    "If Not `path.isdir`, Make Directories".

    Args:
        p (str): [description]
    """

    pd = path.dirname(p)
    if (pd) and (not path.isdir(pd)):
        makedirs(pd)
        if ls:
            ls.append(pd)
    return p


def ivnd(var: Any, de: Any) -> Any:
    """
    If Var is None, return Default else var.

    Args:
        var (Any): Variable to check if it is None.
        de (Any): Default value to return if var is None.

    Returns:
        Any: var if var is not None else de.
    """
    if var is None:
        return de
    return var


def repl(s: str, repl_dict: dict[str, list[str]]) -> str:
    op = s
    for k, v in repl_dict.items():
        if v:
            for i in v:
                op = op.replace(i, k)
    return op


def run(s: str):
    call(shlex.split(s))


def noop(*args, **kwargs):
    pass


def vls_str(vls: list[str | int]) -> list[str]:
    """
    Given the list of version numbers, convert them to their string representation both in modified semver form and semver-compliant form.

    Args:
    - vls (`list[str | int]`): List of version numbers.

    Returns:
    `list[str]`: List of string representation of given list of version numbers, both in modified semver form and semver-compliant form.
    """
    pr = ""
    if vls[4] < 3:
        pr = f"-{PR[vls[4]]}.{vls[5]}"
    return [
        ".".join([str(i) for i in vls[0:4]]) + pr,
        ".".join([str(i) for i in [*vls[0:2], 3 ** vls[2] * 2 ** vls[3]]]) + pr,
    ]
