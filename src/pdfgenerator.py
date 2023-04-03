# From https://weasyprint.readthedocs.io/en/stable/tips-tricks.html
# Modified to accept CSS

import logging
import sys
from math import ceil
from typing import Final, Optional

from weasyprint import CSS, HTML

# Register Loggers
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

logger = logging.getLogger("weasyprint")
logger.setLevel(logging.INFO)

handler.setFormatter(formatter)
logger.addHandler(handler)

# Constants
EXT_VERTICAL_MARGIN = 10

# https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units#lengths
DPI: Final[int] = 96
UNITS_TO_PX: Final[dict[str, int | float]] = {
    "px": 1,
    "in": DPI,
    "pc": DPI / 6,
    "pt": DPI / 72,
}
UNITS_TO_PX["cm"] = CM_TO_PX = (DPI * 25.2) / 64
UNITS_TO_PX["mm"] = MM_TO_PX = CM_TO_PX / 10
UNITS_TO_PX["Q"] = MM_TO_PX / 4
OVERLAY_LAYOUT_TPL: Final[
    str
] = """
@page {size: %s; margin: 0;}
header {position: fixed; top: 0; left: 0; right: 0;}
footer {position: fixed; bottom: 0; left: 0; right: 0;}
"""
PRINT_LAYOUT_TPL: Final[
    str
] = """
@page {{size: {size}; margin: {margin};}}
@page :nth(1) {{size: {size}; margin: {first_margin};}}
"""
COMPUTE_ELEMENT_HF_TPL: Final[
    str
] = """
footer, header {{counter-increment: page {} pages {};}}
"""

# Derived Constants
UNITS: Final[list[str]] = list(UNITS_TO_PX.keys())


def calc_margin(margin: list[float], header_height: int, footer_height: int) -> str:
    header_height += EXT_VERTICAL_MARGIN
    footer_height += EXT_VERTICAL_MARGIN
    match len(margin):
        case 1:
            tm = margin[0]
            margin = [tm + header_height, tm, tm + footer_height]
        case 2:
            vm, hm = margin
            margin = [vm + header_height, hm, vm + footer_height]
        case 3:
            tm, hm, bm = margin
            margin = [tm + header_height, hm, bm + footer_height]
        case 4:
            tm, rm, bm, lm = margin
            margin = [tm + header_height, rm, bm + footer_height, lm]
    return " ".join(f"{i}px" for i in margin)


def margin_preprocessor(margin: list[str]) -> list[float]:  # noqa: C901
    if (not (isinstance(margin, list) or isinstance(margin, tuple))) or (
        len(margin) not in list(range(1, 4 + 1))
    ):
        raise Exception("margin", margin, "list (or tuple) and of length 1-4")

    op = []

    for i in margin:
        for j in UNITS:
            if i.endswith(j):
                break
        else:
            raise Exception("margin", margin, i)

        if len(j) == len(i):
            raise Exception("margin", margin, i)

        ic = i[: -len(j)]
        try:
            op.append(UNITS_TO_PX[j] * float(ic))
        except ValueError:
            raise Exception("margin", margin, i) from None

    return op


def get_element(boxes, element):  # type: ignore[no-untyped-def]
    """
    Given a set of boxes representing the elements of a PDF page in a DOM-like way, find the box which is named `element`.

    Notes:
    - When Weasyprint renders an html into a PDF, it goes though several intermediate steps. Here, in this class, we deal mostly with a box representation: 1 `Document` have 1 `Page` or more, each `Page` 1 `Box` or more. Each box can contain other box. Hence the recursive method `get_element` for example. For more, visit the following links:
        - https://weasyprint.readthedocs.io/en/stable/hacking.html#dive-into-the-source
        - https://weasyprint.readthedocs.io/en/stable/hacking.html#formatting-structure
    """
    for box in boxes:
        if box.element_tag == element:
            return box
        return get_element(box.all_children(), element)


class PDFGenerator:
    """
    Generate a PDF out of a rendered template, with the possibility to integrate nicely a header and a footer if provided.

    Notes:
    - Warning: the logic of this class relies heavily on the internal Weasyprint API. This snippet was written at the time of the release 47, it might break in the future.
    - This generator draws its inspiration and, also a bit of its implementation, from this discussion in the library github issues: https://github.com/Kozea/WeasyPrint/issues/92
    - Hello from whi_ne (https://github.com/whinee) in the past, modified slightly at the time of release 51. And yes, I struggled adding my own features.
    """

    def __init__(
        self,
        *,
        main_html: str,
        stylesheets: list[str],
        first_page_header_html: str,
        first_page_footer_html: str,
        header_html: str,
        footer_html: str,
        base_url: str,
        size: str,
        margin: list[str],
    ) -> None:
        """
        Initialize PDF Generator.

        Notes:
        - The `size` and `margin` arguments are applied to the PDF like CSS does. See https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size and https://developer.mozilla.org/en-US/docs/Web/CSS/margin#syntax respectively for more details.

        Args:
        - main_html (`str`): An HTML file (most of the time a template rendered into a string) which represents the core of the PDF to generate.
        - first_page_header_html (`str`): Optional HTML for the first page's header.
        - first_page_footer_html (`str`): Optional HTML for the first page's footer.
        - header_html (`str`): Optional HTML for header.
        - footer_html (`str`): Optional HTML for footer.
        - base_url (`str`): An absolute url to the page which serves as a reference to Weasyprint to fetch assets, required to get our media.
        - stylesheets (`list[str]`): Optional paths to stylesheets to be used for rendering the PDF.
        - size (`str`): CSS size property applied directly to each page.
        - margin (`str`): CSS margin property applied directly to each page.
        """

        self.main_html = main_html
        self.first_page_header_html = (
            f"<header>{first_page_header_html}</header>"
            if first_page_header_html is not None
            else None
        )
        self.first_page_footer_html = (
            f"<footer>{first_page_footer_html}</footer>"
            if first_page_footer_html is not None
            else None
        )
        self.header_html = (
            f"<header>{header_html}</header>" if header_html is not None else None
        )
        self.footer_html = (
            f"<footer>{footer_html}</footer>" if footer_html is not None else None
        )
        self.base_url = base_url
        self.stylesheets = stylesheets
        self.size = size
        self.margin = margin_preprocessor(margin)
        self.overlay_layout = OVERLAY_LAYOUT_TPL % size

    def _compute_element(  # type: ignore[no-untyped-def]
        self,
        element: str,
        element_string: str,
        page: int,
        pages: int,
    ):
        """
        Compute element in HTML.

        Args:
        - element (`str`): Element's name.
        - element_string (`str`): Element's content.
        - page (`int`): Page number.
        - pages (`int`): Total number of pages.

        Returns:
        `BlockBox`: Weasyprint pre-render of an html element
        """

        html = HTML(string=element_string, base_url=self.base_url)
        element_doc = html.render(
            stylesheets=[
                CSS(
                    string="footer, header {margin:"
                    + " ".join(f"{i}px" for i in self.margin)
                    + ";}",
                ),
                CSS(string=self.overlay_layout),
                CSS(string=COMPUTE_ELEMENT_HF_TPL.format(page, pages)),
                *self.stylesheets,
            ],
        )
        element_page = element_doc.pages[0]
        element_body = get_element(element_page._page_box.all_children(), "body")
        element_body = element_body.copy_with_children(element_body.all_children())
        return element_body

    def _compute_overlay_element(
        self,
        element: str,
        element_string: Optional[str],
    ) -> int:
        """
        Compute overlay element.

        Set self.`element`_body, self.`element`_height to element's content and height, else if element is not found, set to `None`, `0` respectively.

        Args:
        - element (`str`): Element to be computed
        """

        if not element_string:
            element_height = 0
            """`int`: Height of this element, will be translated in a html height"""
        else:
            element_body = self._compute_element(element, element_string, 1, 1)
            element_html = get_element(element_body.all_children(), element)
            element_height = element_html.height
        return ceil(element_height)

    def _apply_overlay_on_main(self, main_doc) -> None:  # type: ignore[no-untyped-def]
        for page_number, page in enumerate(main_doc.pages, start=1):
            page_body = get_element(page._page_box.all_children(), "body")
            if page_number == 1:
                header = self.first_page_header_html
                footer = self.first_page_footer_html
            else:
                header = self.header_html
                footer = self.footer_html

            if header:
                page_body.children += self._compute_element(
                    "header",
                    header,
                    page_number,
                    len(main_doc.pages),
                ).all_children()
            if footer:
                page_body.children += self._compute_element(
                    "footer",
                    footer,
                    page_number,
                    len(main_doc.pages),
                ).all_children()

    def render_pdf(self) -> bytes:
        """
        Return the rendered PDF.

        Returns:
        `bytes`: The rendered PDF.
        """

        margin = self.margin
        comp_first_margin = calc_margin(
            margin,
            self._compute_overlay_element("header", self.first_page_header_html),
            self._compute_overlay_element("footer", self.first_page_footer_html),
        )
        comp_margin = calc_margin(
            margin,
            self._compute_overlay_element("header", self.header_html),
            self._compute_overlay_element("footer", self.footer_html),
        )

        html = HTML(string=self.main_html, base_url=self.base_url)
        main_doc = html.render(
            stylesheets=[
                CSS(
                    string=PRINT_LAYOUT_TPL.format(
                        size=self.size,
                        margin=comp_margin,
                        first_margin=comp_first_margin,
                    ),
                ),
                *self.stylesheets,
            ],
        )

        self._apply_overlay_on_main(main_doc)

        pdf: bytes = main_doc.write_pdf()
        return pdf
