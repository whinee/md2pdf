from typing import Any, Final

from markdown import markdown
from weasyprint import CSS

try:
    from .info import PROJECT_NAME, TW
    from .md_pp import WhExtension
    from .pdfgenerator import PDFGenerator
    from .utils import exceptions
    from .utils.base_cli import command, command_group
    from .utils.utils import file_exists
except ImportError:
    from src.info import TW
    from src.md_pp import WhExtension
    from src.pdfgenerator import PDFGenerator
    from src.utils import exceptions
    from src.utils.base_cli import command, command_group
    from src.utils.utils import file_exists

# Constants
CSS_SCALABLE_SIZE_LS: Final[list[str]] = ["auto", "portrait", "landscape"]
MD_EXT: Final[list[str]] = [
    WhExtension(),
    # 'markdown_katex',
    "extra",
    "codehilite",
]
MD_EXT_CFG: Final[dict[str, Any]] = {
    "markdown_katex": {
        "no_inline_svg": False,
        "insert_fonts_css": True,
    },
}
MD_HF_EXT: Final[list[str]] = ["extra"]
MD_HF_EXT_CFG: Final[dict[str, Any]] = {}


@command_group(
    name=PROJECT_NAME,
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli(**kwargs: dict[str, Any]) -> None:
    """Main command group."""


ccli = command(cli)


def mc(raw_md: str, md_path: str, hf: bool | None = None) -> str | None:
    """
    Markdown chooser.

    Return first argument that is not `None` and convert it into HTML.

    Args:
    ----
    - raw_md (`str`): Raw Markdown string.
    - md_path (`str`): Path to Markdown file.

    Returns:
    -------
    `string`: Raw HTML string.
    """

    if hf is None:
        hf = False
    if (raw_md is None) and md_path is not None:
        with open(file_exists(md_path)) as f:
            raw_md = f.read()
    if raw_md is not None:
        return markdown(raw_md, extensions=MD_HF_EXT if hf else MD_EXT, extension_configs=MD_HF_EXT_CFG if hf else MD_EXT_CFG)  # type: ignore[no-any-return]
    return ""


def hmc(
    raw_html: str,
    html_path: str,
    raw_md: str,
    md_path: str,
    hf: bool | None = None,
) -> str:
    """
    HTML or Markdown chooser.

    Return first argument that is not `None` and convert it into HTML, if it is not already.

    Args:
    - raw_html (`str`): Raw HTML string.
    - html_path (`str`): Path to HTML file.
    - raw_md (`str`): Raw Markdown string.
    - md_path (`str`): Path to Markdown file.

    Returns:
    `string`: Raw HTML string.
    """

    if raw_html is not None:
        return raw_html
    if html_path:
        with open(file_exists(html_path)) as f:
            return f.read()
    return mc(raw_md, md_path, hf)


@ccli
def convert(  # type: ignore[no-untyped-def]  # noqa: C901
    # Input Arguments
    pdf,
    md_raw,
    md_path,
    css_path,
    css_raw,
    ## Markdown Header and Footer
    ### First Page Header and Footer
    md_first_page_header_raw,
    md_first_page_header_path,
    md_first_page_footer_raw,
    md_first_page_footer_path,
    ### General Header and Footer
    md_header_raw,
    md_header_path,
    md_footer_raw,
    md_footer_path,
    ## HTML Header and Footer
    ### First Page Header and Footer
    html_first_page_header_raw,
    html_first_page_header_path,
    html_first_page_footer_raw,
    html_first_page_footer_path,
    ### General Header and Footer
    html_header_raw,
    html_header_path,
    html_footer_raw,
    html_footer_path,
    # General Arguments
    output_html,
    # PDF Renderer Arguments
    base_url,
    dimension,
    orientation,
    margin,
) -> None:
    """
    Converts input markdown to styled HTML and renders it to a PDF file.

    Arguments are explained in the CLI help page.

    Notes
    -----
    - The following is the precedence order of header and footer application (`>` means "precedes"):
        - For header:
            `header_raw` > `header_path` > `md_header_raw` > `md_header_path`
        - For footer:
            `footer_raw` > `footer_path` > `md_footer_raw` > `md_footer_path`
        For the first page of the PDF, the `first_page` arguments precedes all, with precedence order that looks like above.
    - The `dimension` and `orientation` arguments are applied to the PDF like CSS does. See https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size for more details.
    - The `margin` paramater is applied to every page of the PDF like CSS does. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin#syntax for more details. For the summary, refer below:
        - When one value is specified, it applies the same margin to all four sides.
        - When two values are specified, the first value applies to the top and bottom, the second to the left and right.
        - When three values are specified, the first value applies to the top, the second to the right and left, the third to the bottom.
        - When four values are specified, the margins apply to the top, right, bottom, and left in that order (clockwise).

    """

    # Process/Validate Arguments
    stylesheets = [
        *[CSS(filename=file_exists(i)) for i in css_path],
        *[CSS(string=i) for i in css_raw],
    ]
    if all(i is None for i in [md_raw, md_path]):
        err_msg = "Both flags `md_raw` and `md_path` are empty."
        raise exceptions.GeneralExceptions.ValidationError.Common(err_msg)

    ## Convert Header and Footer to HTML (if it is not already)
    raw_header = hmc(
        html_header_raw,
        html_header_path,
        md_header_raw,
        md_header_path,
        True,
    )
    raw_first_page_header = hmc(
        html_first_page_header_raw,
        html_first_page_header_path,
        md_first_page_header_raw,
        md_first_page_header_path,
        True,
    )
    if raw_first_page_header is None:
        raw_first_page_header = raw_header
    raw_footer = hmc(
        html_footer_raw,
        html_footer_path,
        md_footer_raw,
        md_footer_path,
        True,
    )
    raw_first_page_footer = hmc(
        html_first_page_footer_raw,
        html_first_page_footer_path,
        md_first_page_footer_raw,
        md_first_page_footer_path,
        True,
    )
    if raw_first_page_footer is None:
        raw_first_page_footer = raw_footer

    # Convert Markdown to HTML
    raw_html = mc(md_raw, md_path)

    # Validate Converted HTML
    if (raw_html is None) or (not len(raw_html)):
        err_msg = (
            "Input markdown seems to be empty, try checking its contents and try again."
        )
        raise exceptions.GeneralExceptions.ValidationError.Common(err_msg)

    # Process Arguments
    if (
        (orientation is not None)
        and (" " not in dimension)
        and (dimension not in CSS_SCALABLE_SIZE_LS)
    ):
        size = f"{dimension} {orientation}"
    else:
        size = dimension

    # Optional Print HTML to stdout
    if output_html:
        print(f"\n{'=' * TW}\n{pdf}\n{'=' * TW}")

        if raw_first_page_header:
            print(f"{raw_first_page_header}\n{'-' * TW}")
        if raw_header:
            print(f"{raw_header}\n{'-' * TW}")

        print(raw_html)

        if raw_first_page_footer:
            print(f"{'-' * TW}\n{raw_first_page_footer}")
        if raw_footer:
            print(f"{'-' * TW}\n{raw_footer}")

        print("=" * TW)

    pdf_generator = PDFGenerator(
        main_html=raw_html,
        stylesheets=stylesheets,
        first_page_header_html=raw_first_page_header,
        first_page_footer_html=raw_first_page_footer,
        header_html=raw_header,
        footer_html=raw_footer,
        base_url=base_url,
        size=size,
        margin=margin,
    )

    with open(pdf, "wb") as pdf_file:
        pdf_file.write(pdf_generator.render_pdf())
