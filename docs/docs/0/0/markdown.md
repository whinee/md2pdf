<h1 align="center" style="font-weight: bold">
    Markdown Implementation
</h1>


<div class="toc"><h2 id="toc"><b><a href="#toc">Table of Contents</a></b></h2>
<ul><li><a href="#base-implementation">Base Implementation</a></li><li><a href="#extended-syntax">Extended Syntax</a><ul><li><a href="#extended-syntax-math-expression">Math Expression</a></li></ul></li></ul></div>

<h2 id="base-implementation"><b><a href="#base-implementation">Base Implementation</a></b></h2>

md2pdf uses <code><a target="_blank" href="https://github.com/Python-Markdown/markdown">Python-Markdown/markdown</a></code> to convert Markdown to HTML which, apparently, is a Python implementation of <a target="_blank" href="https://daringfireball.net/">John Gruber</a>'s <code><a target="_blank" href="https://daringfireball.net/projects/markdown/">markdown</a></code>

According to the cited program's documentation, the specification is implemented as close to the reference specification as possible. In <a target="_blank" href="https://python-markdown.github.io/#differences">this link</a>, you will see difference of the Python implementation and the original implementation.

And oh yes, this is an arguably messy implementation of Markdown, as opposed to <a target="_blank" href="https://commonmark.org/">Commonmark Markdown</a>. But we got to make do of what we have, no? baka baka :3

<h2 id="extended-syntax"><b><a href="#extended-syntax">Extended Syntax</a></b></h2>

md2pdf extended the base implementation, and hereinunder are the details.

<h3 id="extended-syntax-math-expression"><b><a href="#extended-syntax-math-expression">Math Expression</a></b></h3>

[KaTeX](https://katex.org) expressions are supported in this program. You just need to surround it in a code block, with the language set as `math`. An example of this is the following:

````md
```math
% \f is defined as #1f(#2) using the macro
\f\relax{x} = \int_{-\infty}^\infty
    \f\hat\xi\,e^{2 \pi i \xi x}
    \,d\xi
```
````

[This link](https://katex.org/docs/supported.html) lists all of the supported functions in KaTeX, grouped logically.
