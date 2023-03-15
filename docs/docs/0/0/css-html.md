<h1 align="center" style="font-weight: bold">
    CSS/HTML Stuff
</h1>


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#html-structure">HTML structure</a></li><li><a href="#page-breaks">Page Breaks</a></li></ul></div>

<h2 id="html-structure"><b><a href="#html-structure">HTML structure</a></b></h2>

As I, the developer of this project, only got the core of this project, more specifically the PDF generator part, from [c4ffein](https://github.com/c4ffein)'s [txt2pdf](https://github.com/c4ffein/txt2pdf), I do not know how it truly works.

But from my understanding, to apply the headers and footers, each page is iterated over then the the header and footer is appended as a child of the page's `body` element. Such as that the HTML structure of a page looks like this:

```html
<body>
    ...
    <header>...</header>
    <footer>...</footer>
</body>
```

Well, now that you know, this might be what is messing with your CSS stylesheet. Or maybe CSS is really that shitty, huh? Or maybe it is an exclusively ***me*** problem?

<h2 id="page-breaks"><b><a href="#page-breaks">Page Breaks</a></b></h2>

For more information on how whi~nyaan! came up with the idea of page breaks, refer to [this link](considerations.md#page-breaks).

For details on how to use the page break, refer to [this link](markdown.md#extended-syntax-page-breaks)

The page break is converted to the following HTML:

```html
<div class="pagebreak" style="clear: both; page-break-after: always;"></div>
```

And as such, you can use the following CSS selector to select pagebreaks:

```css
div.pagebreak
```

This is particularly useful for when you want to apply top margins to headings, except for when a pagebreak precedes one.

```css
h1:not(div.pagebreak+h1) {
    margin-top: 50px;
}
```

The CSS ruleset above means that the PDF converter should add a 50px top margin to an H1 heading unless a pagebreak precedes it.
