# **[src](../index.md).[utils](../utils.md).[utils](utils.md)**

    

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-dnrp" id="func-dnrp">dnrp</a></b></h3>

```python
(file: str, n: Optional[int] = None) ‑> str
```

    
Get the directory component of a pathname by n times recursively then return it.

    
<h3><b><i><a href="#func-dnrp-args" id="func-dnrp-args">Args:</a></i></b></h3>

- file (`str`): File to get the directory of.
- n (`Optional[int]`, optional): Number of times to get up the directory???? Defaults to 1.

    
<h3><b><i><a href="#func-dnrp-returns" id="func-dnrp-returns">Returns:</a></i></b></h3>

`str`: The directory component got recursively by n times from the given pathname

    

    
<h3><b><a href="#func-dpop" id="func-dpop">dpop</a></b></h3>

```python
(d: dict[typing.Any, typing.Any], pop: list[int | list[str | int | tuple[str, ...]] | str], de: Optional[Any] = None) ‑> Any
```

    
Iterate through the preferred order of precedence (`pop`) and see if the value exists in the dictionary. If it does, return it. If not, return `de`.

    
<h3><b><i><a href="#func-dpop-args" id="func-dpop-args">Args:</a></i></b></h3>

- d (`Dict[Any, Any]`): Dictionary to retrieve the value from.
- pop (`list[int | tuple[str | int | tuple] | str]`): List of keys to iterate through.
- de (`Any`, optional): Default object to be returned. Defaults to None.

    
<h3><b><i><a href="#func-dpop-returns" id="func-dpop-returns">Returns:</a></i></b></h3>

`Any`: Retrieved value.

    

    
<h3><b><a href="#func-dt" id="func-dt">dt</a></b></h3>

```python
(dt: str, format: str) ‑> str
```

    
Remove timezone from datetime and format it to ISO 8601 format.

    
<h3><b><i><a href="#func-dt-args" id="func-dt-args">Args:</a></i></b></h3>

- dt (`str`): Unformatted datetime string to be formatted to ISO 8601 format
- format (`str`): The initial format of the datetime string

    
<h3><b><i><a href="#func-dt-returns" id="func-dt-returns">Returns:</a></i></b></h3>

`str`: Formatted datetime string

    

    
<h3><b><a href="#func-dt_ts" id="func-dt_ts">dt_ts</a></b></h3>

```python
(ts: str) ‑> str
```

    
Convert the given unix timestamp to ISO 8601 format.

    
<h3><b><i><a href="#func-dt_ts-args" id="func-dt_ts-args">Args:</a></i></b></h3>

- ts (`str`): unix timestamp to be converted to ISO 8601 format

    
<h3><b><i><a href="#func-dt_ts-returns" id="func-dt_ts-returns">Returns:</a></i></b></h3>

`str`: Formatted datetime string

    

    
<h3><b><a href="#func-file_exists" id="func-file_exists">file_exists</a></b></h3>

```python
(fp: str) ‑> str
```

    
Check if the given file path exists.

    
<h3><b><i><a href="#func-file_exists-args" id="func-file_exists-args">Args:</a></i></b></h3>

- fp (`str`): File path to check if it exists.

    
<h3><b><i><a href="#func-file_exists-raises" id="func-file_exists-raises">Raises:</a></i></b></h3>

- `exceptions.GeneralExceptions.ValidationError.FileNotFound`: Raised when a file in the path is not found.

    
<h3><b><i><a href="#func-file_exists-returns" id="func-file_exists-returns">Returns:</a></i></b></h3>

`str`: Return `fp` when file path exists.

    

    
<h3><b><a href="#func-fill_ls" id="func-fill_ls">fill_ls</a></b></h3>

```python
(*, ls: Sequence[Any], length: int, filler: Optional[Any] = None) ‑> Sequence[Any]
```

    
Fill given list (`ls`) with `filler` up to `length`.

    
<h3><b><i><a href="#func-fill_ls-args" id="func-fill_ls-args">Args:</a></i></b></h3>

- ls (`types.SequenceAny`): List to fill with `filler` up to `length`
- length (`int`): Length of the list to achieve.
- filler (`Optional[Any]`, optional): Filler to use. Defaults to `None`.

    
<h3><b><i><a href="#func-fill_ls-returns" id="func-fill_ls-returns">Returns:</a></i></b></h3>

`types.SequenceAny`: Filled list.

    

    
<h3><b><a href="#func-inmd" id="func-inmd">inmd</a></b></h3>

```python
(p: str, ls: Optional[list[str]] = None) ‑> str
```

    
"If Not `os.path.isdir`, Make Directories"

    
<h3><b><i><a href="#func-inmd-args" id="func-inmd-args">Args:</a></i></b></h3>

- p (`str`): The path to be created, if it does not exist.
- ls(`Optional[list[str]]`, optional): List to append directories to that are not found and successfully created. Defaults to None.

    
<h3><b><i><a href="#func-inmd-returns" id="func-inmd-returns">Returns:</a></i></b></h3>

`str`: The path given.

    

    
<h3><b><a href="#func-iter_ls_with_items" id="func-iter_ls_with_items">iter_ls_with_items</a></b></h3>

```python
(ls: list[typing.Any], *items: list[typing.Any]) ‑> Generator[tuple[Any, ...], None, None]
```

    

    

    
<h3><b><a href="#func-ivnd" id="func-ivnd">ivnd</a></b></h3>

```python
(var: Any, de: Any) ‑> Any
```

    
If Var is None, return Default else var.

    
<h3><b><i><a href="#func-ivnd-args" id="func-ivnd-args">Args:</a></i></b></h3>

- var (`Any`): Variable to check if it is None.
- de (`Any`): Default value to return if var is None.

    
<h3><b><i><a href="#func-ivnd-returns" id="func-ivnd-returns">Returns:</a></i></b></h3>

`Any`: var if var is not None else de.

    

    
<h3><b><a href="#func-le" id="func-le">le</a></b></h3>

```python
(expr: str) ‑> Any
```

    
Literal Evaluation

    
<h3><b><i><a href="#func-le-args" id="func-le-args">Args:</a></i></b></h3>

- expr (`str`): Expression to be evaluated.

    
<h3><b><i><a href="#func-le-returns" id="func-le-returns">Returns:</a></i></b></h3>

`Any`: Expression literally evaluated.

    

    
<h3><b><a href="#func-noop" id="func-noop">noop</a></b></h3>

```python
(*args: list[typing.Any], **kwargs: dict[str, typing.Any]) ‑> None
```

    
No operation

    

    
<h3><b><a href="#func-noop_single_kwargs" id="func-noop_single_kwargs">noop_single_kwargs</a></b></h3>

```python
(arg: Any) ‑> Any
```

    

    

    
<h3><b><a href="#func-repl" id="func-repl">repl</a></b></h3>

```python
(s: str, repl_dict: dict[str, list[str]]) ‑> str
```

    
Iterate through the dictionary, find the values in the given string and replace it with the corresponding key, and output the modified string.

    
<h3><b><i><a href="#func-repl-args" id="func-repl-args">Args:</a></i></b></h3>

- s (`str`): String to modify.
- repl_dict (`dict[str, list[str]]`): key-value pairs to replace string within the given string.

    
<h3><b><i><a href="#func-repl-returns" id="func-repl-returns">Returns:</a></i></b></h3>

`str`: Modified string.

    

    
<h3><b><a href="#func-rfnn" id="func-rfnn">rfnn</a></b></h3>

```python
(*args: list[typing.Any]) ‑> Any
```

    
Return First Non-None

Return the first argument that is not `None`, else return `None`.

    
<h3><b><i><a href="#func-rfnn-returns" id="func-rfnn-returns">Returns:</a></i></b></h3>

`Any`: The first argument that is not `None`, else `None`.

    

    
<h3><b><a href="#func-run_mp" id="func-run_mp">run_mp</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Any]) ‑> list[typing.Any]
```

    

    

    
<h3><b><a href="#func-run_mp_qgr" id="func-run_mp_qgr">run_mp_qgr</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Any]) ‑> tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

    

    

    
<h3><b><a href="#func-run_mp_qir" id="func-run_mp_qir">run_mp_qir</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Any], callback: Callable[..., Any]) ‑> None
```

    
Run `multiprocessing.Pool().map_async()`, and quit in return.

Iterate over `iterable` and apply iterated item to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

This function requires the given function to return a bool, or an iterable with its first item as a bool. This bool is then used to decide whether to trigger the callback and terminate the pool.

    

    
<h3><b><a href="#func-run_mp_star" id="func-run_mp_star">run_mp_star</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Iterable[Any]]) ‑> list[typing.Any]
```

    

    

    
<h3><b><a href="#func-run_mp_star_qgr" id="func-run_mp_star_qgr">run_mp_star_qgr</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Iterable[Any]]) ‑> tuple[None] | tuple[typing.Any] | tuple[typing.Any, ...]
```

    

    

    
<h3><b><a href="#func-run_mp_star_qir" id="func-run_mp_star_qir">run_mp_star_qir</a></b></h3>

```python
(func: Callable[..., Any], iterable: Iterable[Iterable[Any]], callback: Callable[..., Any]) ‑> None
```

    
Run `multiprocessing.Pool().starmap_async()`, and quit in return.

Iterate over `iterable` and apply iterated items to `func` asynchronously. Wait for a single process in the pool to return, and terminate the pool.

    

    
<h3><b><a href="#func-sanitize_text" id="func-sanitize_text">sanitize_text</a></b></h3>

```python
(s: str) ‑> str
```

    
Sanitize input text.

Reference: https://stackoverflow.com/a/93029

    
<h3><b><i><a href="#func-sanitize_text-args" id="func-sanitize_text-args">Args:</a></i></b></h3>

- s (`str`): Text to be sanitized.

    
<h3><b><i><a href="#func-sanitize_text-returns" id="func-sanitize_text-returns">Returns:</a></i></b></h3>

`str`: Sanitized text.

    

    
<h3><b><a href="#func-squery" id="func-squery">squery</a></b></h3>

```python
(query: str, possibilities: list[str], cutoff: int | float = 0.6, *, processor: Callable[[Any], Any] = <function <lambda>>) ‑> Generator[tuple[None, str] | tuple[float, str], None, None]
```

    
Custom search query.

    
<h3><b><i><a href="#func-squery-args" id="func-squery-args">Args:</a></i></b></h3>

- query (`str`): String to search for in the possibilities.
- possibilities (`list[str]`): The possibilities to search from.
- cutoff (`int | float`, optional): The minimum percentage of similarity from the given possibilities. Defaults to `0.6`.
- processor (`Callable[[Any], Any]`, optional): Processes the possibilities before comparing it with the query. Defaults to `lambda x: x`.

    
<h3><b><i><a href="#func-squery-returns" id="func-squery-returns">Returns:</a></i></b></h3>

`Generator[tuple[None, str] | tuple[float, str], None, None]`: Generator object of mastching search quries.

    

    
<h3><b><a href="#func-str2int" id="func-str2int">str2int</a></b></h3>

```python
(s: str) ‑> Optional[int]
```

    
If given string is decimal, convert string to integer, else return False.

    
<h3><b><i><a href="#func-str2int-args" id="func-str2int-args">Args:</a></i></b></h3>

    s (str): string to convert to integer.

    
<h3><b><i><a href="#func-str2int-returns" id="func-str2int-returns">Returns:</a></i></b></h3>

    bool: _description_

    

    
<h3><b><a href="#func-which_ls" id="func-which_ls">which_ls</a></b></h3>

```python
(cmd: str, mode: Optional[int] = None, path: str | None = None) ‑> Union[tuple[str], tuple[str, ...], ForwardRef(None)]
```

    
Yoinked from shutil. Given a command, mode, and a PATH string, return the path which
conforms to the given mode on the PATH, or None if there is no such
file.

`mode` defaults to os.F_OK | os.X_OK. `path` defaults to the result
of os.environ.get("PATH"), or can be overridden with a custom search
path.

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-CallbackGetResult" id="class-CallbackGetResult">CallbackGetResult</a></b></h3>

```python
()
```

    

    
<h3><b><i><a href="#class-CallbackGetResult-func" id="class-CallbackGetResult-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-CallbackGetResult-func-callback" id="class-CallbackGetResult-func-callback">callback</a></h3>

```python
(self, *args: list[typing.Any]) ‑> None
```

    

    

    
<h3><a href="#class-CallbackGetResult-func-get" id="class-CallbackGetResult-func-get">get</a></h3>

```python
(self) ‑> tuple[None] | tuple[typing.Any, ...]
```

    

    
<h3><b><a href="#class-ExtInquirerControl" id="class-ExtInquirerControl">ExtInquirerControl</a></b></h3>

```python
(choices: Sequence[Union[str, questionary.prompts.common.Choice, Dict[str, Any]]], default: Union[str, questionary.prompts.common.Choice, Dict[str, Any], ForwardRef(None)] = None, pointer: str | None = '»', use_indicator: bool = True, use_shortcuts: bool = False, show_selected: bool = False, use_arrow_keys: bool = True, initial_choice: Union[str, questionary.prompts.common.Choice, Dict[str, Any], ForwardRef(None)] = None, **kwargs: Any)
```

    
Control that displays formatted text. This can be either plain text, an
:class:`~prompt_toolkit.formatted_text.HTML` object an
:class:`~prompt_toolkit.formatted_text.ANSI` object, a list of ``(style_str,
text)`` tuples or a callable that takes no argument and returns one of
those, depending on how you prefer to do the formatting. See
``prompt_toolkit.layout.formatted_text`` for more information.

(It's mostly optimized for rather small widgets, like toolbars, menus, etc...)

When this UI control has the focus, the cursor will be shown in the upper
left corner of this control by default. There are two ways for specifying
the cursor position:

- Pass a `get_cursor_position` function which returns a `Point` instance
  with the current cursor position.

- If the (formatted) text is passed as a list of ``(style, text)`` tuples
  and there is one that looks like ``('[SetCursorPosition]', '')``, then
  this will specify the cursor position.

Mouse support:

    The list of fragments can also contain tuples of three items, looking like:
    (style_str, text, handler). When mouse support is enabled and the user
    clicks on this fragment, then the given handler is called. That handler
    should accept two inputs: (Application, MouseEvent) and it should
    either handle the event or return `NotImplemented` in case we want the
    containing Window to handle this event.

:param focusable: `bool` or :class:`.Filter`: Tell whether this control is
    focusable.

:param text: Text or formatted text to be displayed.
:param style: Style string applied to the content. (If you want to style
    the whole :class:`~prompt_toolkit.layout.Window`, pass the style to the
    :class:`~prompt_toolkit.layout.Window` instead.)
:param key_bindings: a :class:`.KeyBindings` object.
:param get_cursor_position: A callable that returns the cursor position as
    a `Point` instance.

    
<h3><b><i><a href="#class-ExtInquirerControl-mro" id="class-ExtInquirerControl-mro">Ancestors (in MRO)</a></i></b></h3>

* questionary.prompts.common.InquirerControl
* prompt_toolkit.layout.controls.FormattedTextControl
* prompt_toolkit.layout.controls.UIControl

    
<h3><b><i><a href="#class-ExtInquirerControl-cvar" id="class-ExtInquirerControl-cvar">Class variables</a></i></b></h3>

    
`answer_text`

    
<h3><b><a href="#class-ExtQuestion" id="class-ExtQuestion">ExtQuestion</a></b></h3>

```python
(application: Application[Any])
```

    
A question to be prompted.

This is an internal class. Questions should be created using the
predefined questions (e.g. text or password).

    
<h3><b><i><a href="#class-ExtQuestion-mro" id="class-ExtQuestion-mro">Ancestors (in MRO)</a></i></b></h3>

* questionary.question.Question

    
<h3><b><i><a href="#class-ExtQuestion-cvar" id="class-ExtQuestion-cvar">Class variables</a></i></b></h3>

    
`kbi`

    
<h3><b><i><a href="#class-ExtQuestion-func" id="class-ExtQuestion-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-ExtQuestion-func-ask" id="class-ExtQuestion-func-ask">ask</a></h3>

```python
(self, patch_stdout: bool | None = None, **kwargs: dict[str, typing.Any]) ‑> tuple[bool, typing.Any]
```

    
Ask the question synchronously and return user response.

    
<h3><i><a href="#class-ExtQuestion-func-ask-args" id="class-ExtQuestion-func-ask-args">Args:</a></i></h3>

- patch_stdout (`bool`, optional): Ensure that the prompt renders correctly if other threads are printing to stdout. Defaults to `None`.

    
<h3><i><a href="#class-ExtQuestion-func-ask-returns" id="class-ExtQuestion-func-ask-returns">Returns:</a></i></h3>

`Any`: The answer from the question.

    
<h3><b><a href="#class-PoolTerminate" id="class-PoolTerminate">PoolTerminate</a></b></h3>

```python
(pool: multiprocessing.pool.Pool, callback: Callable[..., Any])
```

    

    
<h3><b><i><a href="#class-PoolTerminate-func" id="class-PoolTerminate-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-PoolTerminate-func-inner" id="class-PoolTerminate-func-inner">inner</a></h3>

```python
(self, err: bool, *args: list[typing.Any], **kwargs: dict[str, typing.Any]) ‑> None
```