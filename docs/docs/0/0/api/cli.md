# **[src](index.md).[cli](cli.md)**

    

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-hmc" id="func-hmc">hmc</a></b></h3>

```python
(raw_html: str, html_path: str, raw_md: str, md_path: str, hf: bool | None = None) ‑> str
```

    
HTML or Markdown chooser.

Return first argument that is not `None` and convert it into HTML, if it is not already.

    
<h3><b><i><a href="#func-hmc-args" id="func-hmc-args">Args:</a></i></b></h3>

- raw_html (`str`): Raw HTML string.
- html_path (`str`): Path to HTML file.
- raw_md (`str`): Raw Markdown string.
- md_path (`str`): Path to Markdown file.

    
<h3><b><i><a href="#func-hmc-returns" id="func-hmc-returns">Returns:</a></i></b></h3>

`string`: Raw HTML string.

    

    
<h3><b><a href="#func-mc" id="func-mc">mc</a></b></h3>

```python
(raw_md: str, md_path: str, hf: bool | None = None) ‑> str | None
```

    
Markdown chooser.

Return first argument that is not `None` and convert it into HTML.

    
<h3><b><i><a href="#func-mc-args" id="func-mc-args">Args:</a></i></b></h3>

----
- raw_md (`str`): Raw Markdown string.
- md_path (`str`): Path to Markdown file.

    
<h3><b><i><a href="#func-mc-returns" id="func-mc-returns">Returns:</a></i></b></h3>

-------
`string`: Raw HTML string.