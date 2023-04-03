import ast
import difflib
import itertools
import os
import re
import shutil
import sys
import unicodedata
from collections.abc import Callable, Generator
from datetime import datetime, timedelta
from multiprocessing import Pool, pool
from os import makedirs
from os.path import dirname as dn
from os.path import realpath as rp
from re import Pattern
from time import strftime, strptime
from typing import Any, Final, Optional

import arrow
from questionary.constants import (
    DEFAULT_KBI_MESSAGE,
    INDICATOR_SELECTED,
    INDICATOR_UNSELECTED,
)
from questionary.prompts.common import Choice, InquirerControl, Separator
from questionary.question import Question
from rich import print

try:
    from ..info import PSH
    from . import exceptions, types
except ImportError:
    from src.info import PSH
    from src.utils import exceptions, types


# Constants
CATEGORIES: Final[set[str]] = {"Cn"}

# Derived Constants
ALL_CHARS: Final[Generator[str, None, None]] = (chr(i) for i in range(sys.maxunicode))
CCHARS: Final[str] = "".join(
    map(chr, itertools.chain(range(0x00, 0x20), range(0x7F, 0xA0))),
)
CCHARS_RE: Final[Pattern[str]] = re.compile("[%s]" % re.escape(CCHARS))


# Class
class PoolTerminate:
    def __init__(self, pool: pool.Pool, callback: types.CallableAny) -> None:
        self.called = False
        self.pool = pool
        self.callback = callback

    def inner(self, err: bool, *args: types.Args, **kwargs: types.Kwargs) -> None:
        if err and (not self.called):
            self.called = True
            self.pool.terminate()
            self.callback(*args, **kwargs)


class CallbackGetResult:
    def __init__(self) -> None:
        self.args: tuple[None] | tuple[Any, ...] = ()

    def callback(self, *args: types.Args) -> None:
        self.args = args

    def get(self) -> tuple[None] | tuple[Any, ...]:
        return self.args


class ExtInquirerControl(InquirerControl):  # type: ignore[misc]
    answer_text = "Answer"

    def _get_choice_tokens(self) -> list[Any]:  # noqa: C901
        tokens: list[Any] = []

        def append(index: int, choice: Choice) -> None:  # noqa: C901
            # use value to check if option has been selected
            selected = choice.value in self.selected_options

            if index == self.pointed_at:
                if self.pointer is not None:
                    tokens.append(("class:pointer", " {} ".format(self.pointer)))
                else:
                    tokens.append(("class:text", " " * 3))

                tokens.append(("[SetCursorPosition]", ""))
            else:
                pointer_length = len(self.pointer) if self.pointer is not None else 1
                tokens.append(("class:text", " " * (2 + pointer_length)))

            if isinstance(choice, Separator):
                tokens.append(("class:separator", "{}".format(choice.title)))
            elif choice.disabled:  # disabled
                if isinstance(choice.title, list):
                    tokens.append(
                        ("class:selected" if selected else "class:disabled", "- "),
                    )
                    tokens.extend(choice.title)
                else:
                    tokens.append(
                        (
                            "class:selected" if selected else "class:disabled",
                            "- {}".format(choice.title),
                        ),
                    )

                tokens.append(
                    (
                        "class:selected" if selected else "class:disabled",
                        "{}".format(
                            ""
                            if isinstance(choice.disabled, bool)
                            else " ({})".format(choice.disabled),
                        ),
                    ),
                )
            else:
                shortcut = choice.get_shortcut_title() if self.use_shortcuts else ""  # type: ignore[no-untyped-call]

                if selected:
                    if self.use_indicator:
                        indicator = INDICATOR_SELECTED + " "
                    else:
                        indicator = ""

                    tokens.append(("class:selected", "{}".format(indicator)))
                else:
                    if self.use_indicator:
                        indicator = INDICATOR_UNSELECTED + " "
                    else:
                        indicator = ""

                    tokens.append(("class:text", "{}".format(indicator)))

                if isinstance(choice.title, list):
                    tokens.extend(choice.title)
                elif selected:
                    tokens.append(
                        ("class:selected", "{}{}".format(shortcut, choice.title)),
                    )
                elif index == self.pointed_at:
                    tokens.append(
                        ("class:highlighted", "{}{}".format(shortcut, choice.title)),
                    )
                else:
                    tokens.append(("class:text", "{}{}".format(shortcut, choice.title)))

            tokens.append(("", "\n"))

        # prepare the select choices
        for i, c in enumerate(self.choices):
            append(i, c)

        if self.show_selected:
            current = self.get_pointed_at()

            answer = ""

            answer += (
                current.title if isinstance(current.title, str) else current.title[0][1]  # type: ignore[index]
            )

            tokens.append(("class:text", f"  {self.answer_text}: " + answer))
        else:
            tokens.pop()  # Remove last newline.
        return tokens


class ExtQuestion(Question):  # type: ignore[misc]
    kbi = DEFAULT_KBI_MESSAGE

    def ask(self, patch_stdout: Optional[bool] = None, **kwargs: dict[str, Any]) -> tuple[bool, Any]:  # type: ignore[override]
        """
        Ask the question synchronously and return user response.

        Args:
        - patch_stdout (`bool`, optional): Ensure that the prompt renders correctly if other threads are printing to stdout. Defaults to `None`.

        Returns:
        `Any`: The answer from the question.
        """

        if patch_stdout is None:
            patch_stdout = False

        if self.should_skip_question:
            return True, self.default

        try:
            return True, self.unsafe_ask(patch_stdout)
        except KeyboardInterrupt:
            print("\n{}\n".format(self.kbi))
            return False, None


# Functions
def dnrp(file: str, n: Optional[int] = None) -> str:
    """
    Get the directory component of a pathname by n times recursively then return it.

    Args:
    - file (`str`): File to get the directory of.
    - n (`Optional[int]`, optional): Number of times to get up the directory???? Defaults to 1.

    Returns:
    `str`: The directory component got recursively by n times from the given pathname
    """
    op = rp(file)
    for _ in range(ivnd(n, 1)):
        op = dn(op)
    return op


def dpop(
    d: dict[Any, Any],
    pop: list[int | list[str | int | tuple[str, ...]] | str],
    de: Optional[Any] = None,
) -> Any:
    """
    Iterate through the preferred order of precedence (`pop`) and see if the value exists in the dictionary. If it does, return it. If not, return `de`.

    Args:
    - d (`Dict[Any, Any]`): Dictionary to retrieve the value from.
    - pop (`list[int | tuple[str | int | tuple] | str]`): List of keys to iterate through.
    - de (`Any`, optional): Default object to be returned. Defaults to None.

    Returns:
    `Any`: Retrieved value.
    """

    for i in pop:
        if op := d.get(i):
            return op
    return de


def dt(dt: str, format: str) -> str:
    """
    Remove timezone from datetime and format it to ISO 8601 format.

    Args:
    - dt (`str`): Unformatted datetime string to be formatted to ISO 8601 format
    - format (`str`): The initial format of the datetime string

    Returns:
    `str`: Formatted datetime string
    """

    if "ago" in dt and not format:
        dt = arrow.utcnow().dehumanize(dt)  # type: ignore
    tz = re.match(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})([-+])(\d{2}):(\d{2})", dt)
    if tz:
        iso, s, ho, mo = tz.groups()
        s = -1 if s == "-" else 1
        op = (
            datetime.fromisoformat(iso)
            - (s * timedelta(hours=int(ho), minutes=int(mo)))
        ).strftime("%Y-%m-%dT%H:%M:%S")
    else:
        op = strftime("%Y-%m-%dT%H:%M:%S", strptime(dt, format))
    return op


def dt_ts(ts: str) -> str:
    """
    Convert the given unix timestamp to ISO 8601 format.

    Args:
    - ts (`str`): unix timestamp to be converted to ISO 8601 format

    Returns:
    `str`: Formatted datetime string
    """

    return (datetime.utcfromtimestamp(int(ts))).strftime("%Y-%m-%dT%H:%M:%S")


def file_exists(fp: str) -> str:
    """
    Check if the given file path exists.

    Args:
    - fp (`str`): File path to check if it exists.

    Raises:
    - `exceptions.GeneralExceptions.ValidationError.FileNotFound`: Raised when a file in the path is not found.

    Returns:
    `str`: Return `fp` when file path exists.
    """
    if not os.path.exists(fp):
        raise exceptions.GeneralExceptions.ValidationError.FileNotFound(fp)
    return fp


def fill_ls(
    *,
    ls: types.SequenceAny,
    length: int,
    filler: Optional[Any] = None,
) -> types.SequenceAny:
    """
    Fill given list (`ls`) with `filler` up to `length`.

    Args:
    - ls (`types.SequenceAny`): List to fill with `filler` up to `length`
    - length (`int`): Length of the list to achieve.
    - filler (`Optional[Any]`, optional): Filler to use. Defaults to `None`.

    Returns:
    `types.SequenceAny`: Filled list.
    """
    lls = len(ls)
    if lls < length:
        return ls

    return [*ls, *[filler for _ in range(length - lls)]]


def inmd(p: str, ls: Optional[list[str]] = None) -> str:
    """
    "If Not `os.path.isdir`, Make Directories".

    Args:
    - p (`str`): The path to be created, if it does not exist.
    - ls(`Optional[list[str]]`, optional): List to append directories to that are not found and successfully created. Defaults to None.

    Returns:
    `str`: The path given.
    """

    pd = os.path.dirname(p)
    if (pd) and (not os.path.isdir(pd)):
        makedirs(pd)
        if ls:
            ls.append(pd)
    return p


def iter_ls_with_items(
    ls: types.ListAny,
    *items: types.ListAny,
) -> Generator[tuple[Any, ...], None, None]:
    for i in ls:
        yield i, *items


def ivnd(var: Any, de: Any) -> Any:
    """
    If Var is None, return Default else var.

    Args:
    - var (`Any`): Variable to check if it is None.
    - de (`Any`): Default value to return if var is None.

    Returns:
    `Any`: var if var is not None else de.
    """
    if var is None:
        return de
    return var


def le(expr: str) -> Optional[Any]:
    """
    Literal Evaluation.

    Args:
    - expr (`str`): Expression to be evaluated.

    Returns:
    `Any`: Expression literally evaluated.
    """
    if expr is not None:
        return ast.literal_eval(expr)


def noop(*args: types.ListAny, **kwargs: dict[str, Any]) -> None:
    """No operation."""


def noop_single_kwargs(arg: Any) -> Any:
    return arg


def repl(s: str, repl_dict: dict[str, list[str]]) -> str:
    """
    Iterate through the dictionary, find the values in the given string and replace it with the corresponding key, and output the modified string.

    Args:
    - s (`str`): String to modify.
    - repl_dict (`dict[str, list[str]]`): key-value pairs to replace string within the given string.

    Returns:
    `str`: Modified string.
    """
    op = s
    for k, v in repl_dict.items():
        for i in v:
            op = op.replace(i, k)
    return op


def rfnn(*args: types.ListAny) -> Any:
    """
    Return First Non-None.

    Return the first argument that is not `None`, else return `None`.

    Returns:
    `Any`: The first argument that is not `None`, else `None`.
    """
    for i in args:
        if i is not None:
            return i


def run_mp(func: types.CallableAny, iterable: types.IterAny) -> types.ListAny:
    with Pool() as pool:
        return pool.map(func, iterable)


def run_mp_star(func: types.CallableAny, iterable: types.IterIterAny) -> types.ListAny:
    with Pool() as pool:
        return pool.starmap(func, iterable)


def run_mp_qir(
    func: types.CallableAny,
    iterable: types.IterAny,
    callback: types.CallableAny,
) -> None:
    """
    Run `multiprocessing.Pool().map_async()`, and quit in return.

    Iterate over `iterable` and apply iterated item to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

    This function requires the given function to return a bool, or an iterable with its first item as a bool. This bool is then used to decide whether to trigger the callback and terminate the pool.
    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        for i in iterable:
            pool.apply_async(
                func,
                args=(i,),
                callback=PoolTerminate(pool, callback).inner,
            )
        pool.close()
        pool.join()


def run_mp_star_qir(
    func: types.CallableAny,
    iterable: types.IterIterAny,
    callback: types.CallableAny,
) -> None:
    """
    Run `multiprocessing.Pool().starmap_async()`, and quit in return.

    Iterate over `iterable` and apply iterated items to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.
    """
    if callback is None:
        callback = noop
    with Pool() as pool:
        for i in iterable:
            pool.apply_async(func, args=i, callback=PoolTerminate(pool, callback).inner)
        pool.close()
        pool.join()


def run_mp_qgr(func: types.CallableAny, iterable: types.IterAny) -> types.TupleAny:
    res_cb = CallbackGetResult()
    run_mp_qir(func, iterable, res_cb.callback)
    return res_cb.get()


def run_mp_star_qgr(
    func: types.CallableAny,
    iterable: types.IterIterAny,
) -> types.TupleAny:
    res_cb = CallbackGetResult()
    run_mp_star_qir(func, iterable, res_cb.callback)
    return res_cb.get()


def sanitize_text(s: str) -> str:
    """
    Sanitize input text.

    Reference: https://stackoverflow.com/a/93029

    Args:
    - s (`str`): Text to be sanitized.

    Returns:
    `str`: Sanitized text.
    """
    return unicodedata.normalize("NFKD", CCHARS_RE.sub("", s)).strip()


def str2int(s: str) -> Optional[int]:
    """
    If given string is decimal, convert string to integer, else return False.

    Args:
        s (str): string to convert to integer.

    Returns:
        bool: _description_
    """
    if s[0] in ("-", "+") and s[1:].isdecimal():
        return int(s)
    if s.isdecimal():
        return int(s)
    return None


def squery(
    query: str,
    possibilities: list[str],
    cutoff: int | float = 0.6,
    *,
    processor: Callable[[Any], Any] = lambda x: x,
) -> Generator[tuple[None, str] | tuple[float, str], None, None]:
    """
    Custom search query.

    Args:
    - query (`str`): String to search for in the possibilities.
    - possibilities (`list[str]`): The possibilities to search from.
    - cutoff (`int | float`, optional): The minimum percentage of similarity from the given possibilities. Defaults to `0.6`.
    - processor (`Callable[[Any], Any]`, optional): Processes the possibilities before comparing it with the query. Defaults to `lambda x: x`.

    Returns:
    `Generator[tuple[None, str] | tuple[float, str], None, None]`: Generator object of mastching search quries.
    """

    sequence_matcher = difflib.SequenceMatcher()
    sequence_matcher.set_seq2(query)

    for search_value in possibilities:
        sequence_matcher.set_seq1(processor(search_value))
        if query.lower() in processor(search_value).lower():
            yield (None, search_value)
            continue
        if (
            sequence_matcher.real_quick_ratio() >= cutoff
            and sequence_matcher.quick_ratio() >= cutoff
            and sequence_matcher.ratio() >= cutoff
        ):
            yield (sequence_matcher.ratio(), search_value)


def which_ls(  # noqa: C901
    cmd: str,
    mode: Optional[int] = os.F_OK | os.X_OK,
    path: Optional[str] = os.environ.get("PATH", None),  # noqa: B008
) -> Optional[types.TupleStr]:
    """
    Given a command, mode, and a PATH string, return the path which conforms to the given mode on the PATH, or None if there is no such file.

    Notes:
    - Yoinked from shutil.
    - `mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
    of os.environ.get("PATH"), or can be overridden with a custom search
    path.

    Args:
    - cmd (`str`): Executable to look for.
    - mode (`Optional[int]`, optional): Executable permissions to look for. Defaults to `os.F_OK | os.X_OK`.
    - path (`Optional[str]`, optional): The PATH to where the executable can be found. Defaults to `os.environ.get("PATH", None)`.

    Returns:
    `Optional[types.TupleStr]`: List of path where executable is found at.
    """

    # If we're given a path with a directory part, look it up directly rather
    # than referring to PATH directories. This includes checking relative to the
    # current directory, e.g. ./script
    if os.path.dirname(cmd):
        if shutil._access_check(cmd, mode):
            return (cmd,)
        return None

    if path is None:
        try:
            path = os.confstr("CS_PATH")
        except (AttributeError, ValueError):
            # os.confstr() or CS_PATH is not available
            path = os.defpath

    # PATH='' doesn't match, whereas PATH=':' looks in the current directory
    if not path:
        return None

    path = os.fsdecode(path).split(os.pathsep)  # type: ignore[assignment]

    if PSH == "win":
        curdir = os.curdir
        if curdir not in path:
            path.insert(0, curdir)

        # PATHEXT is necessary to check on Windows.
        pathext_source = os.getenv("PATHEXT") or shutil._WIN_DEFAULT_PATHEXT
        pathext = [ext for ext in pathext_source.split(os.pathsep) if ext]

        # See if the given file matches any of the expected path extensions.
        # This will allow us to short circuit when given "python.exe".
        # If it does match, only test that one, otherwise we have to try
        # others.
        if any(cmd.lower().endswith(ext.lower()) for ext in pathext):
            files = [cmd]
        else:
            files = [cmd + ext for ext in pathext]
    else:
        # On other platforms you don't have things like PATHEXT to tell you
        # what file suffixes are executable, so just pass on cmd as-is.
        files = [cmd]

    seen = set()
    op = set()
    for dir in path:
        normdir = os.path.normcase(dir)
        if normdir not in seen:
            seen.add(normdir)
            for thefile in files:
                name = os.path.join(dir, thefile)
                if shutil._access_check(name, mode):
                    op.add(name)
    return tuple(op)
