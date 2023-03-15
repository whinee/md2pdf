# **[src](index.md).[md_pp](md_pp.md)**

    

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-get_bin_cmd" id="func-get_bin_cmd">get_bin_cmd</a></b></h3>

```python
() ‑> list[str]
```

    

    

    
<h3><b><a href="#func-htmlsvg2img" id="func-htmlsvg2img">htmlsvg2img</a></b></h3>

```python
(html: str) ‑> str
```

    

    

    
<h3><b><a href="#func-katex2html" id="func-katex2html">katex2html</a></b></h3>

```python
(marker: str, tex: str) ‑> tuple[str, str]
```

    

    

    
<h3><b><a href="#func-make_marker_id" id="func-make_marker_id">make_marker_id</a></b></h3>

```python
(text: str) ‑> str
```

    

    

    
<h3><b><a href="#func-mdblocks_katex2img" id="func-mdblocks_katex2img">mdblocks_katex2img</a></b></h3>

```python
(mdblocks: dict[str, str]) ‑> list[typing.Any]
```

    

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-GeneralFencedBlockPostprocessor" id="class-GeneralFencedBlockPostprocessor">GeneralFencedBlockPostprocessor</a></b></h3>

```python
(md: str, ext: src.md_pp.WhExtension)
```

    
Postprocessors are run after the ElementTree it converted back into text.

Each Postprocessor implements a "run" method that takes a pointer to a
text string, modifies it as necessary and returns a text string.

Postprocessors must extend markdown.Postprocessor.

    
<h3><b><i><a href="#class-GeneralFencedBlockPostprocessor-mro" id="class-GeneralFencedBlockPostprocessor-mro">Ancestors (in MRO)</a></i></b></h3>

* markdown.postprocessors.Postprocessor
* markdown.util.Processor

    
<h3><b><i><a href="#class-GeneralFencedBlockPostprocessor-func" id="class-GeneralFencedBlockPostprocessor-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-GeneralFencedBlockPostprocessor-func-run" id="class-GeneralFencedBlockPostprocessor-func-run">run</a></h3>

```python
(self, text: str) ‑> str
```

    
Subclasses of Postprocessor should implement a `run` method, which
takes the html document as a single text string and returns a
(possibly modified) string.

    
<h3><b><a href="#class-KatexFencedBlockPostprocessor" id="class-KatexFencedBlockPostprocessor">KatexFencedBlockPostprocessor</a></b></h3>

```python
(md: str, ext: src.md_pp.WhExtension)
```

    
Postprocessors are run after the ElementTree it converted back into text.

Each Postprocessor implements a "run" method that takes a pointer to a
text string, modifies it as necessary and returns a text string.

Postprocessors must extend markdown.Postprocessor.

    
<h3><b><i><a href="#class-KatexFencedBlockPostprocessor-mro" id="class-KatexFencedBlockPostprocessor-mro">Ancestors (in MRO)</a></i></b></h3>

* markdown.postprocessors.Postprocessor
* markdown.util.Processor

    
<h3><b><i><a href="#class-KatexFencedBlockPostprocessor-func" id="class-KatexFencedBlockPostprocessor-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-KatexFencedBlockPostprocessor-func-run" id="class-KatexFencedBlockPostprocessor-func-run">run</a></h3>

```python
(self, text: str) ‑> str
```

    
Subclasses of Postprocessor should implement a `run` method, which
takes the html document as a single text string and returns a
(possibly modified) string.

    
<h3><b><a href="#class-KatexFencedBlockPreprocessor" id="class-KatexFencedBlockPreprocessor">KatexFencedBlockPreprocessor</a></b></h3>

```python
(md: str, ext: src.md_pp.WhExtension)
```

    
Preprocessors are run after the text is broken into lines.

Each preprocessor implements a "run" method that takes a pointer to a
list of lines of the document, modifies it as necessary and returns
either the same pointer or a pointer to a new list.

Preprocessors must extend markdown.Preprocessor.

    
<h3><b><i><a href="#class-KatexFencedBlockPreprocessor-mro" id="class-KatexFencedBlockPreprocessor-mro">Ancestors (in MRO)</a></i></b></h3>

* markdown.preprocessors.Preprocessor
* markdown.util.Processor

    
<h3><b><i><a href="#class-KatexFencedBlockPreprocessor-func" id="class-KatexFencedBlockPreprocessor-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-KatexFencedBlockPreprocessor-func-run" id="class-KatexFencedBlockPreprocessor-func-run">run</a></h3>

```python
(self, lines: list[str]) ‑> list[str]
```

    
Each subclass of Preprocessor should override the `run` method, which
takes the document as a list of strings split by newlines and returns
the (possibly modified) list of lines.

    
<h3><b><a href="#class-WhExtension" id="class-WhExtension">WhExtension</a></b></h3>

```python
(**kwargs: dict[str, typing.Any])
```

    
Base class for extensions to subclass. 

Initiate Extension and set up configs.

    
<h3><b><i><a href="#class-WhExtension-mro" id="class-WhExtension-mro">Ancestors (in MRO)</a></i></b></h3>

* markdown.extensions.Extension

    
<h3><b><i><a href="#class-WhExtension-func" id="class-WhExtension-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-WhExtension-func-extendMarkdown" id="class-WhExtension-func-extendMarkdown">extendMarkdown</a></h3>

```python
(self, md: markdown.core.Markdown) ‑> None
```

    
Add the various processors and patterns to the Markdown Instance.

This method must be overridden by every extension.

Keyword arguments:

* md: The Markdown instance.

* md_globals: Global variables in the markdown module namespace.

    

    
<h3><a href="#class-WhExtension-func-reset" id="class-WhExtension-func-reset">reset</a></h3>

```python
(self) ‑> None
```