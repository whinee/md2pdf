# **[src](index.md).[pdfgenerator](pdfgenerator.md)**

    

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-calc_margin" id="func-calc_margin">calc_margin</a></b></h3>

```python
(margin: list[float], header_height: int, footer_height: int) ‑> str
```

    

    

    
<h3><b><a href="#func-get_element" id="func-get_element">get_element</a></b></h3>

```python
(boxes, element)
```

    
Given a set of boxes representing the elements of a PDF page in a DOM-like way, find the box which is named `element`.

Notes:
- When Weasyprint renders an html into a PDF, it goes though several intermediate steps. Here, in this class, we deal mostly with a box representation: 1 `Document` have 1 `Page` or more, each `Page` 1 `Box` or more. Each box can contain other box. Hence the recursive method `get_element` for example. For more, visit the following links:
    - https://weasyprint.readthedocs.io/en/stable/hacking.html#dive-into-the-source
    - https://weasyprint.readthedocs.io/en/stable/hacking.html#formatting-structure

    

    
<h3><b><a href="#func-margin_preprocessor" id="func-margin_preprocessor">margin_preprocessor</a></b></h3>

```python
(margin: list[str]) ‑> list[float]
```

    

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-PDFGenerator" id="class-PDFGenerator">PDFGenerator</a></b></h3>

```python
(*, main_html: str, stylesheets: list[str], first_page_header_html: str, first_page_footer_html: str, header_html: str, footer_html: str, base_url: str, size: str, margin: list[str])
```

    
Generate a PDF out of a rendered template, with the possibility to integrate nicely a header and a footer if provided.

Notes:
- Warning: the logic of this class relies heavily on the internal Weasyprint API. This snippet was written at the time of the release 47, it might break in the future.
- This generator draws its inspiration and, also a bit of its implementation, from this discussion in the library github issues: https://github.com/Kozea/WeasyPrint/issues/92
- Hello from whi_ne (https://github.com/whinee) in the past, modified slightly at the time of release 51. And yes, I struggled adding my own features.

Initialize PDF Generator.

Notes:
- The `size` and `margin` arguments are applied to the PDF like CSS does. See https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size and https://developer.mozilla.org/en-US/docs/Web/CSS/margin#syntax respectively for more details.

    
<h3><b><i><a href="#class-PDFGenerator-args" id="class-PDFGenerator-args">Args:</a></i></b></h3>

- main_html (`str`): An HTML file (most of the time a template rendered into a string) which represents the core of the PDF to generate.
- first_page_header_html (`str`): Optional HTML for the first page's header.
- first_page_footer_html (`str`): Optional HTML for the first page's footer.
- header_html (`str`): Optional HTML for header.
- footer_html (`str`): Optional HTML for footer.
- base_url (`str`): An absolute url to the page which serves as a reference to Weasyprint to fetch assets, required to get our media.
- stylesheets (`list[str]`): Optional paths to stylesheets to be used for rendering the PDF.
- size (`str`): CSS size property applied directly to each page.
- margin (`str`): CSS margin property applied directly to each page.

    
<h3><b><i><a href="#class-PDFGenerator-func" id="class-PDFGenerator-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-PDFGenerator-func-render_pdf" id="class-PDFGenerator-func-render_pdf">render_pdf</a></h3>

```python
(self) ‑> bytes
```

    
Return the rendered PDF.

    
<h3><i><a href="#class-PDFGenerator-func-render_pdf-returns" id="class-PDFGenerator-func-render_pdf-returns">Returns:</a></i></h3>

`bytes`: The rendered PDF.