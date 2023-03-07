# **[src](../index.md).[utils](../utils.md).[style](style.md)**

    

    
<h2><b><a href="#var" id="var">Variables</a></b></h2>

    
`COLORS`
t1: F3F78D
t2: FF8D5C
t3: E84855
t4: B56B45
t5: 404E7C
t6: 55828B
t7: 4E8098

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-pp" id="func-pp">pp</a></b></h3>

```python
(t: Any, ca: bool | None = None, *args: list[typing.Any], **kwargs: dict[str, typing.Any]) ‑> None
```

    
Center rich printable objects, then pretty print it.

    
<h3><b><i><a href="#func-pp-args" id="func-pp-args">Args:</a></i></b></h3>

- t (`Any`): Rich printable object to be centered, then pretty printed.
- ca (`bool`, optional): Determines whether to center text in the group individually. Defaults to `None`.

    

    
<h3><b><a href="#func-split_text" id="func-split_text">split_text</a></b></h3>

```python
(t: str) ‑> list[str]
```

    

    

    
<h3><b><a href="#func-text" id="func-text">text</a></b></h3>

```python
(t: str, *args: list[typing.Any], ca: bool | None = None, **kwargs: dict[str, typing.Any]) ‑> rich.console.Group
```

    

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-C" id="class-C">C</a></b></h3>

```python
()
```

    

    
<h3><b><i><a href="#class-C-cvar" id="class-C-cvar">Class variables</a></i></b></h3>

    
`h0`

    
`h1`

    
`h2`

    
`s0`

    
`s1`

    
`s2`

    
<h3><b><a href="#class-S" id="class-S">S</a></b></h3>

```python
()
```

    

    
<h3><b><i><a href="#class-S-cvar" id="class-S-cvar">Class variables</a></i></b></h3>

    
`p0`

    
`p1`

    
`p_critical`

    
`p_error`

    
`p_warning`

    
`t0`

    
`t1`

    
`t2`

    
`t3`

    
`t4`

    
`t5`

    
`t6`

    
`t_critical`

    
`t_error`

    
`t_good`

    
`t_warning`

    
<h3><b><a href="#class-ct" id="class-ct">ct</a></b></h3>

```python
()
```

    

    
<h3><b><i><a href="#class-ct-sfunc" id="class-ct-sfunc">Static methods</a></i></b></h3>

    

    
<h3><a href="#class-ct-func-group" id="class-ct-func-group">group</a></h3>

```python
(*ls: rich.console.ConsoleRenderable | rich.console.RichCast | str) ‑> rich.console.Group
```

    
Group given list of rich printable objects.

    
<h3><i><a href="#class-ct-func-group-returns" id="class-ct-func-group-returns">Returns:</a></i></h3>

`Group`: Group of rich printable objects

    

    
<h3><a href="#class-ct-func-table" id="class-ct-func-table">table</a></h3>

```python
(cols: list[str], rows: list[list[str]]) ‑> None
```

    
Print table from given list of str and list of list of strings for the columns and rows respectively.

    
<h3><i><a href="#class-ct-func-table-args" id="class-ct-func-table-args">Args:</a></i></h3>

- cols (`list[str]`): List of string for column labels.
- rows (`list[list[str]]`): List of rows (list of strings).