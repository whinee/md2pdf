import re
from collections.abc import Sized
from enum import Enum
from functools import partial
from typing import Any, Optional

try:
    from .info import DEF_STR
    from .utils.exceptions import CDExceptions
    from .utils.utils import str2int
except ImportError:
    from src.info import DEF_STR
    from src.utils.exceptions import CDExceptions
    from src.utils.utils import str2int


# Constants
BEHAVIOR = Enum("BEHAVIOR", ["modify", "insert", "append"])

# Derived Constants
SUB_ALL_INT = partial(re.sub, r"\d+", "")


# @c_exc_str
# class CDInsTypeError(TypeError):
#     def __init__(self, sep: str, og_path: str, idx: int, tck: type) -> None:
#         if tck is list:
#             conc = ", but is not the last element of the path."
#         else:
#             conc = ", expected dictionary or a sized iterable ― that is if the said iterable is the value of the last element in the path."
#         self.message = (
#             f"`{sep.join(og_path.split(sep)[:idx + 1])}` is a " + tck.__name__ + conc
#         )


class CustomDict(dict):  # type: ignore[type-arg]
    """Custom dictionary."""

    def __getitem__(self, key: str) -> Any:
        op = super().__getitem__(key)
        if op.__class__.__mro__[-2] is dict:
            return CustomDict(op)
        return op

    def traverse(  # noqa: C901
        self,
        path: str,
        elem: dict[str, Any] | Sized,
        sep: str,
        idx: int = 0,
        og_path: Optional[str] = None,
    ) -> tuple[int, Any | dict[str, int]] | Any:
        """
        _summary_.

        Return States
        | State \||                              Return Type \||                       Description |
        |--------:|-------------------------------------------:|:----------------------------------|
        |     0 \||                       Any (Indexed Item) \|| Path fully traversed              |
        |     1 \||   dict[str, int] (Kwargs for CDKeyError) \|| Path's not in element             |
        |     2 \|| dict[str, int] (Kwargs for CDIndexError) \|| Path's current index not in range |

        Callback States
        | State \||                             Arguments Type \||                                Description |
        |--------:|---------------------------------------------:|:-------------------------------------------|
        |     0 \||  dict (Indexed Item), str (key), int (idx) \||  Path fully traversed; Element type `dict` |
        |     1 \|| Sized (Indexed Item), int (key), int (idx) \|| Path fully traversed; Element type `Sized` |

        Args:
            path (str): _description_
            elem (dict[str, Any] | Sized): _description_
            sep (str): _description_
            idx (int, optional): _description_. Defaults to 0.
            og_path (Optional[str], optional): _description_. Defaults to None.

        Raises:
            CDKeyError: _description_
            CDKeyError: _description_
            CDKeyError: _description_
            CDIndexError: _description_
            CDTypeError: _description_

        Returns:
            Any: _description_

        ```mermaid
        flowchart TD
            start([start]) --> args[/path, value, elem/] --> a
            a{elem isDict?}
                a --> |yes| b{key in<br>elem}
                    b --> |yes| c{path fully<br>traversed?}
                        c -->
        |no| y[["traverse(<br>path=path[1:],<br>elem=elem[key]<br>)"]]:::success
                        c --> |yes| x[/"(0, elem[key])"/]:::success
                    b --> |no| f([CDKeyError]):::error
                a --> |no| g{elem isSized?}
                    g --> |no| l(["CDTypeError;<br>exp dict/Sized"]):::error
                        h --> |no| m(["CDKeyError;<br>key empty"]):::error
                            i --> |no| n(["CDKeyError;<br>key not int"]):::error
                    g --> |yes| h{"key notEmpty?"}
                        h --> |yes| i{key int?}
                            i --> |yes| j{key inRange?}
                                j -->
        |no| w[/"(1, {'idx': idx, 'ls_idx': ls_idx, 'len_iter': len_iter})"/]:::success
                                j ----> |yes| c

            classDef success color:#83ce9e,stroke:#6fc890
            classDef error color:#f3626b,stroke:#f14651
        ```
        """

        if og_path is None:
            og_path = path

        tc = type(elem).__mro__[-2]
        path_ls = path.split(sep)

        key = path_ls[0]
        is_not_last = len(path_ls) > 1

        if tc is dict:
            if key in elem:  # type: ignore[operator]
                if is_not_last:
                    return self.traverse(
                        path=path.replace(key + sep, "", 1),
                        elem=elem[key],  # type: ignore[index]
                        sep=sep,
                        idx=idx + 1,
                        og_path=og_path,
                    )
                return 0, elem[key]  # type: ignore[index]
            return 1, {"key": key}
        if isinstance(elem, list) or isinstance(elem, tuple):
            if len(key) < 0:
                raise CDExceptions.API.KeyError(
                    "index expected as an integer",
                    f"`{sep.join(og_path.split(sep)[:idx])}`'s indexed element is a sized iterable (type {tc.__name__}); expected index to be an integer, but instead was an empty string.",
                )
            ls_idx = str2int(key)
            if ls_idx is None:
                raise CDExceptions.API.KeyError(
                    "index expected as an integer",
                    f"`{sep.join(og_path.split(sep)[:idx])}` is a sized iterable (type {tc.__name__}); index expected to be an integer, but instead was set to `{key}`.",
                )
            len_iter = len(elem)
            if len_iter > ls_idx > (-1 - len_iter):
                if is_not_last:
                    return self.traverse(
                        path=path.replace(key + sep, "", 1),
                        elem=elem[ls_idx],  # type: ignore[index]
                        sep=sep,
                        idx=idx + 1,
                        og_path=og_path,
                    )
                return 0, elem[ls_idx]
            return 2, {"idx": idx, "ls_idx": ls_idx, "len_iter": len_iter}

        raise CDExceptions.API.TypeError(
            "indexed element expected as dictionary or sized iterable",
            f"`{sep.join(og_path.split(sep)[:idx])}` expected as a dictionary or a sized iterable, instead was `{tc.__name__}`",
        )

    def dir(self, path: str = DEF_STR, de: Any = DEF_STR, sep: str = "/") -> Any:
        if (path == DEF_STR) or (path == ""):
            return self
        state, op = self.traverse(path=path, elem=self, sep=sep)
        match state:
            case 0:
                if isinstance(op, dict):
                    return CustomDict(op)
                return op
            case 1:
                if de != DEF_STR:
                    return de
                raise CDExceptions.API.KeyNotInElement(**op)
            case 2:
                raise CDExceptions.API.IndexError(sep=sep, og_path=path, **op)
            case _:
                CDExceptions.Internals.StateUnexpected(state=state, max_state=1)


def test() -> None:
    # Init Test

    ## Initialize
    test = CustomDict()
    assert test == {}

    ## Initialize with a dict
    test = CustomDict({"a": 1, "b": 2})
    assert test == {"a": 1, "b": 2}

    test = CustomDict({"a": {"b": {"c": 3}}})
    print(test.modify("a/b/c", 4), test)
    assert test == {"a": {"b": {"c": 4}}}

    # Dir Test
    test = CustomDict({"a": {"b": {"c": [1, 2, 3]}}})
    assert test.dir("a/b/c") == [1, 2, 3]
    try:
        test.dir("a/b/c/d")
    except CDExceptions.API.KeyError:
        pass
    else:
        raise AssertionError

    ## Subsequent Dir
    test = CustomDict({"a": {"b": {"c": 3}}})

    test = test.dir("a/b")
    assert test == {"c": 3}

    assert test.dir("c") == 3

    ## Deeply Nested Dicts and Iterables

    # fmt: off
    test = CustomDict({"a": ("shit", "me", {"not": {"lol": [
        "why", "you", ["ask", "?", "cuz", {"why": "naught"}]],
    }})})
    assert test.dir(f"a/-1/not/lol/+2/{0-1}/why") == "naught"
    # fmt: on

    # Modify Test

    test = CustomDict({"a": {"b": {"c": 3}}})
    test.modify("a/b/c", 4)
    assert test == {"a": {"b": {"c": 4}}}

    # dict - dict
    test = CustomDict({"a": {"b": "c"}})
    assert test.modify("a/b", "d") == {"a": {"b": "d"}}

    # dict - list
    test = CustomDict({"a": ["b", "c"]})
    test.modify("a/1", "d")
    assert test.modify("a/1", "d") == {"a": ["b", "d"]}
    assert test.insert("a/1", "d") == {"a": ["b", "d", "c"]}
    test.append("a", "d")
    assert test.append("a", "d") == {"a": ["b", "d", "c", "d"]}

    # list - list
    test = CustomDict({"w": [["a", ["b", "c"]], ["d"]]})
    test.modify("w/0", "as")
    assert test.modify("w/0", "a") == {"w": ["a", ["d"]]}
    assert test.insert("w/0/1/2", "e") == {"w": [["a", ["b", "c", "d"]], ["d"]]}
    assert test.append("w/1", "f") == {"w": [["a", ["b", "c"]], ["d", "f"]]}

    # Insert to an initiliazed dictionary
    test = CustomDict({})
    test.insert("a", 1)
    assert test == {"a": 1}
