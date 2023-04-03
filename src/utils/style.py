import itertools
import textwrap
from functools import partial
from typing import Any, Optional

import rich
from rich.align import Align
from rich.console import Console, ConsoleRenderable, Group, RichCast
from rich.panel import Panel
from rich.style import Style
from rich.table import Column, Table
from rich.text import Text
from yachalk import chalk

try:
    from ..info import TW
except ImportError:
    from src.info import TW

# Constants

COLORS = {
    "h": ["#f2f774", "#ff7b42", "#e83140"],
    "s": ["#F3F78D", "#FF8D5C", "#E84855"],
}

"""t1: F3F78D
  t2: FF8D5C
  t3: E84855
  t4: B56B45
  t5: 404E7C
  t6: 55828B
  t7: 4E8098"""

COLORS_TYPE: dict[str, dict[str, list[str] | dict[str, str]]] = {
    "p": {
        "n": [
            "#E68AFF",
            "#9D7DFF",
        ],
        "named": {
            # f7c16b-f6a54e-f14651
            "warning": "#f7c16b",
            "error": "#f6a54e",
            "critical": "#f14651",
        },
    },
    "t": {
        # "n": [           # OG
        #     "#FFF273",
        #     "#C1ADFF",
        #     "#FF96C1",
        # ],
        "n": [  # Warm
            "#264653",
            "#2A9D8F",
            "#E9C46A",
            "#fcbf49",
            "#F4A261",
            "#E76F51",
            "#d62828",
        ],
        "named": {
            # f8ca7f-f7b36b-f3626b
            "good": "#00b601",
            "warning": "#f8ca7f",
            "error": "#f7b36b",
            "critical": "#f3626b",
        },
    },
}

STYLE_ALL: dict[str, dict[str, Any]] = {
    "all": {"padding": [0, 5]},
    "table": {
        "box": "ROUNDED",
        "row_styles": ["none", "dim"],
        "show_lines": True,
        "title_justify": "center",
        "columns": [
            {
                "header_style": "h0",
                "style": "h0",
            },
            {
                "header_style": "h1",
                "style": "h1",
            },
            {
                "header_style": "h2",
                "style": "h2",
            },
        ],
    },
}

# Derived Constants
CONSOLE: Console = Console(highlight=False)


def split_text(t: str) -> list[str]:
    op = []
    for i in t.split("\n"):
        for j in textwrap.wrap(i, width=TW):
            if j != "":
                op.append(j)
            else:
                op.append("")
    return op


def text(
    t: str,
    *args: list[Any],
    ca: Optional[bool] = None,
    **kwargs: dict[str, Any],
) -> Group:
    fn = partial(Text, *args, **kwargs)
    op = []
    for i in split_text(t):
        ip = fn(i)
        op.append(Align.center(ip) if (ca if ca is not None else True) else ip)
    return Group(*op)  # type: ignore


STYLE_TYPE = {
    "p": Panel,
    "t": text,
}


class S:
    pass


class C:
    pass


# for idx, i in enumerate(COLORS_TYPE["t"]["n"]):
#     setattr(S, f"t{idx}", chalk.hex(i).bold)
#     # setattr(S, f"{k}{idx}", partial(v, style=Style(color=i)))
# for vk, vv in COLORS_TYPE["t"]["named"].items(): # type: ignore[union-attr]
#     setattr(S, f"t_{vk}", partial(text, style=Style(color=vv)))

for k, v in STYLE_TYPE.items():
    for idx, i in enumerate(COLORS_TYPE[k]["n"]):
        setattr(S, f"{k}{idx}", chalk.hex(i).bold)
        # setattr(S, f"{k}{idx}", partial(v, style=Style(color=i)))
    for vk, vv in COLORS_TYPE[k]["named"].items():  # type: ignore[union-attr]
        setattr(S, f"{k}_{vk}", partial(v, style=Style(color=vv)))  # type: ignore

for k, v in COLORS.items():
    for idx, i in enumerate(v):
        setattr(C, f"{k}{idx}", i)


def pp(
    t: Any,
    ca: Optional[bool] = None,
    *args: list[Any],
    **kwargs: dict[str, Any],
) -> None:
    """
    Center rich printable objects, then pretty print it.

    Args:
    - t (`Any`): Rich printable object to be centered, then pretty printed.
    - ca (`bool`, optional): Determines whether to center text in the group individually. Defaults to `None`.
    """
    if ca is None:
        ca = True
    if isinstance(t, str):
        t = text(t, ca)
    CONSOLE.print(Align.center(t) if ca else t, *args, **kwargs)


class ct:
    @staticmethod
    def group(*ls: ConsoleRenderable | RichCast | str) -> Group:
        """
        Group given list of rich printable objects.

        Returns:
        `Group`: Group of rich printable objects
        """
        op = []
        for i in ls:
            op.append(Align.center(i))
        return Group(*op)

    @staticmethod
    def table(cols: list[str], rows: list[list[str]]) -> None:
        """
        Print table from given list of str and list of list of strings for the columns and rows respectively.

        Args:
        - cols (`list[str]`): List of string for column labels.
        - rows (`list[list[str]]`): List of rows (list of strings).
        """
        stb = STYLE_ALL["table"]
        box = getattr(rich.box, stb.pop("box"))

        new_cols = []
        for title, col in zip(cols, itertools.cycle(stb.pop("columns")), strict=False):
            attr = {}
            for i in ["header_style", "style"]:
                attr[i] = getattr(C, col[i])
            new_cols.append(Column(title, **attr, justify="center"))

        t = Table(*new_cols, **stb, **STYLE_ALL["all"], box=box)
        for i in rows:  # type: ignore[assignment]
            t.add_row(*[str(i) for i in i])

        pp(t)
