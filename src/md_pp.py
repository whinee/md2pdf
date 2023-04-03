import base64
import hashlib
import os
import re
import shutil
import signal
import subprocess
import urllib.parse
from collections.abc import Generator
from functools import partial
from glob import glob
from typing import Any

from markdown import Markdown
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor

try:
    from .info import MACHINE, PROJ_ABS_PATH, PSH
    from .utils import exceptions
    from .utils.base_cli import de_rcfg, de_wcfg, get_stg
    from .utils.utils import dnrp, run_mp_star, which_ls
except ImportError:
    from src.info import MACHINE, PROJ_ABS_PATH, PSH
    from src.utils import exceptions
    from src.utils.base_cli import de_rcfg, de_wcfg, get_stg
    from src.utils.utils import dnrp, run_mp_star, which_ls

# Constants
KATEX_CMD_NAME = "katex"
FALLBACK_BIN_DIR = "/usr/local/bin"
NPX_KATEX_FMT = f"{{}} --no-install {KATEX_CMD_NAME}"
KATEX_OPTS = "-t -T -c 'f3626b' -F html".split()


HTML_PAGE_BREAK = (
    """<div class="pagebreak" style="clear: both; page-break-after: always;"></div>"""
)
PAGE_BREAK_REPLACE = partial(
    re.compile(r"^<p>&lt;&lt;&lt;&lt;&gt;&gt;&gt;&gt;<\/p>", re.MULTILINE).sub,
    repl=HTML_PAGE_BREAK,
)

SVG_XMLNS = (
    'xmlns="http://www.w3.org/2000/svg" '
    + 'xmlns:xlink="http://www.w3.org/1999/xlink" '
)
B64IMG_TMPL = '<img src="data:image/svg+xml;base64,{img_text}"/>'

KATEX_STYLESHEET = f"""
<link rel="stylesheet"
    href="file:///{urllib.parse.quote_plus(os.path.join(dnrp(__file__), "katex", "katex.min.css"))}"
/>
<style type="text/css">
    .katex img {{
        object-fit: fill;
        padding: unset;
        display: block;
        position: absolute;
        width: 100%;
        height: inherit;
    }}
    p .katex {{
        display: table;
        margin: 0 auto;
    }}
</style>
"""

# Derived Constants
SIG_NAME_BY_NUM = {
    k: v
    for v, k in sorted(signal.__dict__.items(), reverse=True)
    if v.startswith("SIG") and not v.startswith("SIG_")
}

SEMVER_RE = re.compile(r"\d+\.\d+\.\d+")
SVG_ELEM_RE = re.compile(r"<svg.*?</svg>", flags=re.MULTILINE | re.DOTALL)
FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})")
BLOCK_START_RE = re.compile(r"^(\s*)(`{3,}|~{3,})math")
BLOCK_CLEAN_RE = re.compile(r"^(\s*)(`{3,}|~{3,})math(.*)(\2)$", flags=re.DOTALL)

PKG_BIN_DIR = os.path.join(PROJ_ABS_PATH, "katex", "bin")

# Initialize Variables
KATEX_CMD_PARTS: list[str] = []


def _get_bin_cmd() -> str:  # noqa: C901
    if bin := shutil.which(KATEX_CMD_NAME):
        return bin

    if MACHINE == "AMD64":
        machine = "x86_64"
    else:
        machine = MACHINE
    bin_ls: list[str] = list(glob(f"{PKG_BIN_DIR}/*_{machine}-{PSH}*"))
    if bin_ls:
        return max(bin_ls)

    if npx_bin_ls := which_ls("npx"):
        for i in npx_bin_ls:
            try:
                npx_cmd = NPX_KATEX_FMT.format(i)
                output_data = subprocess.check_output(
                    [*npx_cmd.split(), "--version"],
                    stderr=subprocess.STDOUT,
                )
                output_text = output_data.decode("utf-8")
                if SEMVER_RE.match(output_text.strip()) is None:
                    continue
                return npx_cmd
            except subprocess.CalledProcessError:
                continue
            except OSError:
                continue

    raise exceptions.KatexExceptions.NotFound


def get_bin_cmd() -> list[str]:
    if bin := get_stg("katex_bin", de=None):  # type: ignore[arg-type]
        bin_cmd: list[str] = bin.split()
        if "npx" in bin:
            output_data = subprocess.check_output(
                [*bin_cmd, "--version"],
                stderr=subprocess.STDOUT,
            )
            if SEMVER_RE.match(output_data.decode("utf-8").strip()) is not None:
                return bin_cmd
        if shutil._access_check(bin, os.F_OK | os.X_OK):
            return bin_cmd
    bin = _get_bin_cmd()
    cfg = de_rcfg()
    cfg["katex_bin"] = bin
    de_wcfg(cfg)
    op: list[str] = bin.split()
    return op


def htmlsvg2img(html: str) -> str:
    for match in reversed(tuple(SVG_ELEM_RE.finditer(html))):
        svg_text = match.group(0)
        if "xmlns" not in svg_text:
            svg_text = svg_text.replace("<svg ", "<svg " + SVG_XMLNS)
        svg_data = svg_text.encode("utf-8")
        img_b64_data: bytes = base64.standard_b64encode(svg_data)
        img_b64_text = img_b64_data.decode("utf-8")
        img_b64_tag = B64IMG_TMPL.format(img_text=img_b64_text)
        start, end = match.span()
        html = html[:start] + img_b64_tag + html[end:]

    return html


def katex2html(marker: str, tex: str) -> tuple[str, str]:  # type: ignore[return]
    try:
        proc = subprocess.run(
            KATEX_CMD_PARTS,
            input=tex.encode("utf-8"),
            bufsize=-1,
            capture_output=True,
        )
        ret_code = proc.returncode
        stdout = proc.stdout.decode("utf-8")
        if ret_code < 0:
            signame = SIG_NAME_BY_NUM[abs(ret_code)]
            err_msg = (
                f"Error processing '{tex}': "
                + "katex_cli process ended with "
                + f"code {ret_code} ({signame})"
            )
            raise Exception(err_msg)
        if ret_code > 0:
            errout = proc.stderr.decode("utf-8")
            output = (stdout + "\n" + errout).strip()
            err_msg = f"Error processing '{tex}': {output}"
            raise Exception(err_msg)
        return marker, htmlsvg2img(stdout)
    except Exception:  # noqa: BLE001
        pass


def mdblocks_katex2img(mdblocks: dict[str, str]) -> list[Any]:
    global KATEX_CMD_PARTS
    KATEX_CMD_PARTS = get_bin_cmd() + KATEX_OPTS
    return run_mp_star(katex2html, mdblocks.items())


def make_marker_id(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.md5(data, usedforsecurity=False).hexdigest()


class WhExtension(Extension):  # type: ignore[misc]
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self.math_blocks: dict[str, str] = {}
        super().__init__(**kwargs)

    def reset(self) -> None:
        self.math_blocks.clear()

    def extendMarkdown(self, md: Markdown) -> None:  # noqa: N802
        md.registerExtension(self)
        md.preprocessors.register(
            KatexFencedBlockPreprocessor(md, self),
            "wh_katex_pre",
            25,
        )
        md.postprocessors.register(
            KatexFencedBlockPostprocessor(md, self),
            "wh_katex_post",
            0,
        )
        md.postprocessors.register(
            GeneralFencedBlockPostprocessor(md, self),
            "wh_post",
            0,
        )


class KatexFencedBlockPreprocessor(Preprocessor):  # type: ignore[misc]
    def __init__(self, md: str, ext: WhExtension) -> None:
        super().__init__(md)
        self.ext: WhExtension = ext

    def _make_tag_for_block(self, block_lines: list[str]) -> str:
        indent_len = len(block_lines[0]) - len(block_lines[0].lstrip())
        indent_text = block_lines[0][:indent_len]

        block_text = "\n".join(line[indent_len:] for line in block_lines).rstrip()
        marker_id = make_marker_id("block" + block_text)
        marker_tag = f"tmp_block_md_katex_{marker_id}"

        self.ext.math_blocks[marker_tag] = block_text
        return indent_text + marker_tag

    def _iter_out_lines(  # noqa: C901
        self,
        lines: list[str],
    ) -> Generator[str, None, None]:
        is_in_math_fence = False
        expected_close_fence = "```"

        block_lines: list[str] = []

        for line in lines:
            if is_in_math_fence:
                if line.rstrip() == expected_close_fence:
                    is_in_math_fence = False
                    marker_tag = self._make_tag_for_block(block_lines)
                    del block_lines[:]
                    yield marker_tag
                else:
                    block_lines.append(line)
            elif math_fence_match := BLOCK_START_RE.match(line):
                is_in_math_fence = True
                prefix = math_fence_match.group(1)
                expected_close_fence = prefix + math_fence_match.group(2)
            else:
                yield line

        # unclosed block
        if block_lines:
            for line in block_lines:
                yield line

    def run(self, lines: list[str]) -> list[str]:
        return list(self._iter_out_lines(lines))


class KatexFencedBlockPostprocessor(Postprocessor):  # type: ignore[misc]
    def __init__(self, md: str, ext: WhExtension) -> None:
        super().__init__(md)
        self.ext: WhExtension = ext

    def run(self, text: str) -> str:
        if not any(marker in text for marker in self.ext.math_blocks):
            return text

        # if self.ext.options:
        #     insert_fonts_css = self.ext.options.get("insert_fonts_css", True)
        # else:
        #     insert_fonts_css = True
        #
        if KATEX_STYLESHEET not in text:
            text = KATEX_STYLESHEET + text

        for marker, html in mdblocks_katex2img(self.ext.math_blocks):
            # is_block = marker.startswith("tmp_block_md_katex_")
            # is_inline = marker.startswith("tmp_inline_md_katex_")
            # assert is_block or is_inline
            html = "<p>" + html + "</p>"
            while marker in text:
                text = text.replace("<p>" + marker + "</p>", html)
                text = text.replace(marker, html)

        return text


class GeneralFencedBlockPostprocessor(Postprocessor):  # type: ignore[misc]
    def __init__(self, md: str, ext: WhExtension) -> None:
        super().__init__(md)
        self.ext: WhExtension = ext

    def run(self, text: str) -> str:
        return PAGE_BREAK_REPLACE(string=text)
