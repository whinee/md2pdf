��convert��args��kwargs��help��Convert markdown to pdf�Convert markdown to pdf�arguments��options� �pdf��kwargs��requiredähelp��help�Output PDF file path�md_raw��help��help�+Raw string Markdown to be rendered into PDF�md_path��help��help�*Markdown file path to be rendered into PDF�css_path��kwargs��multipleähelp��help�0CSS file paths to be applied to the rendered PDF�css_raw��kwargs��multipleähelp��help�0Raw string CSS to be applied to the rendered PDF�md_header_raw��help��help�+Optional raw string Markdown for the header�md_header_path��help��help�*Optional Markdown file path for the header�md_footer_raw��help��help�+Optional raw string Markdown for the footer�md_footer_path��help��help�*Optional Markdown file path for the footer�html_header_raw��help��help�'Optional raw string HTML for the header�html_header_path��help��help�&Optional HTML file path for the header�html_footer_raw��help��help�'Optional raw string HTML for the footer�html_footer_path��help��help�&Optional HTML file path for the footer�md_first_page_header_raw��help��help�8Optional raw string Markdown for the first page's header�md_first_page_header_path��help��help�7Optional Markdown file path for the first page's header�md_first_page_footer_raw��help��help�8Optional raw string Markdown for the first page's footer�md_first_page_footer_path��help��help�7Optional Markdown file path for the first page's footer�html_first_page_header_raw��help��help�4Optional raw string HTML for the first page's header�html_first_page_header_path��help��help�3Optional HTML file path for the first page's header�html_first_page_footer_raw��help��help�4Optional raw string HTML for the first page's footer�html_first_page_footer_path��help��help�3Optional HTML file path for the first page's footer�output_html��kwargs��is_flagähelp��help�+Whether to print raw output HTML to console�base_url��help��help�:Absolute base path for markdown linked content (as images)�dimension��kwargs��default�letter�help��help�"Dimension of the rendered PDF. Dimension can be any of the following:
- For scalable sizes:
    `auto`, `portrait`, `landscape`
- length value/s
    Up to two values only, seperated with space. If only one value is given, it will be applied as the width and height of the PDF, else, the two values will be used as width and height of the PDF respectively.
- keyword value:
    - ISO standards:
        `A5`, `A4`, `A3`, `B5`, `B4`
    - JIS standards:
        `JIS-B5`, `JIS-B4`
    - North American Standards:
        `letter`, `legal`, `ledger`�orientation��kwargs��default�portrait�help��help٤Orientation of the rendered PDF.
If a singular length value or a keyword value is passed as `dimension` argument, the PDF size shall be `{dimension} {orientation}`.�margin��kwargs��default��0.5in�multipleähelp��help� CSS margin property applied directly to each page. See https://developer.mozilla.org/en-US/docs/Web/CSS/margin#syntax for more details.
For the summary, refer below:
  - When one value is specified, it applies the same margin to all four sides.
  - When two values are specified, the first value applies to the top and bottom, the second to the left and right.
  - When three values are specified, the first value applies to the top, the second to the right and left, the third to the bottom.
  - When four values are specified, the margins apply to the top, right, bottom, and left in that order (clockwise).
The following are the only allowed units and their conversion to pixels (DPI is set at 96 px):
  123456789 123456789 123456789 123456789 123456789 123456789
  - `cm` (Centimeters):         (`DPI` * 25.2) / 64
  - `in` (Inches):              `DPI`
  - `mm` (Millimeters):         `cm` / 10
  - `pc` (Picas):               `in` / 6
  - `pt` (Points):              `in` / 72
  - `px` (Pixels):              1
  - `Q`  (Quarter-millimeters): `mm` / 4�example�fPassing the following options `--margin 0.5in --margin 0.7in` will yield a CSS margin of `0.5in 0.7in`�credits��args��kwargs��help��credits�!It's the credits, whaddya expect?�arguments��options��version��args��kwargs��help��display application version�3Print version of the program. Useful for debugging.�arguments��options�