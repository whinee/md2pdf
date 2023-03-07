# **[src](../index.md).[utils](../utils.md).[base_cli](base_cli.md)**

    

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-command" id="func-command">command</a></b></h3>

```python
(group: src.utils.base_cli.Group) ‑> Callable[[Callable[..., Any]], Callable[..., Any]]
```

    
Wrapper for click commands.

    
<h3><b><i><a href="#func-command-args" id="func-command-args">Args:</a></i></b></h3>

- group (`Group`): Command group of the command to be under.

    
<h3><b><i><a href="#func-command-returns" id="func-command-returns">Returns:</a></i></b></h3>

- `Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><b><a href="#func-command_group" id="func-command_group">command_group</a></b></h3>

```python
(name: Union[str, Callable[..., Any], ForwardRef(None)] = None, **attrs: Any) ‑> src.utils.base_cli.Group
```

    

    

    
<h3><b><a href="#func-custom_command" id="func-custom_command">custom_command</a></b></h3>

```python
(name: Union[str, Callable[..., Any], ForwardRef(None)] = None, cls: Optional[Type[src.utils.base_cli.Command]] = None, **attrs: Any) ‑> Union[src.utils.base_cli.Command, Callable[..., src.utils.base_cli.Command]]
```

    

    

    
<h3><b><a href="#func-de_rcfg" id="func-de_rcfg">de_rcfg</a></b></h3>

```python
() ‑> src.utils.cd.CustomDict
```

    
Return parsed configuration file, fetched from the CFLOP.

    
<h3><b><i><a href="#func-de_rcfg-returns" id="func-de_rcfg-returns">Returns:</a></i></b></h3>

`dict[Any, Any]`: _description_

    

    
<h3><b><a href="#func-de_wcfg" id="func-de_wcfg">de_wcfg</a></b></h3>

```python
(value: dict[typing.Any, typing.Any] | list[typing.Any]) ‑> None
```

    
Write given value to the configuration file, fetched from the CFLOP.

    
<h3><b><i><a href="#func-de_wcfg-args" id="func-de_wcfg-args">Args:</a></i></b></h3>

- value (`dict[Any, Any] | list[Any]`): dictionary to overwrite the configuration file, fetched from the CFLOP.

    

    
<h3><b><a href="#func-get_stg" id="func-get_stg">get_stg</a></b></h3>

```python
(path: str, **kwargs: dict[str, typing.Any]) ‑> Optional[Any]
```

    

    

    
<h3><b><a href="#func-init" id="func-init">init</a></b></h3>

```python
(idx: int) ‑> None
```

    

    

    
<h3><b><a href="#func-select" id="func-select">select</a></b></h3>

```python
(message: str, choices: Union[Sequence[str | questionary.prompts.common.Choice | dict[str, Any]], dict[str, Any]], default: Optional[Any] = None, instruction: str | None = None, qmark: str | None = None, pointer: str | None = None, style: Optional[prompt_toolkit.styles.base.BaseStyle] = None, show_selected: bool | None = None, ret_err: bool | None = None, **kwargs: dict[str, typing.Any]) ‑> tuple[bool, typing.Any]
```

    

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-Command" id="class-Command">Command</a></b></h3>

```python
(name: str | None, context_settings: Optional[Dict[str, Any]] = None, callback: Optional[Callable[..., Any]] = None, params: Optional[List[ForwardRef('Parameter')]] = None, help: str | None = None, epilog: str | None = None, short_help: str | None = None, options_metavar: str | None = '[OPTIONS]', add_help_option: bool = True, no_args_is_help: bool = False, hidden: bool = False, deprecated: bool = False)
```

    
Commands are the basic building block of command line interfaces in
Click.  A basic command handles command line parsing and might dispatch
more parsing to commands nested below it.

:param name: the name of the command to use unless a group overrides it.
:param context_settings: an optional dictionary with defaults that are
                         passed to the context object.
:param callback: the callback to invoke.  This is optional.
:param params: the parameters to register with this command.  This can
               be either :class:`Option` or :class:`Argument` objects.
:param help: the help string to use for this command.
:param epilog: like the help string but it's printed at the end of the
               help page after everything else.
:param short_help: the short help to use for this command.  This is
                   shown on the command listing of the parent command.
:param add_help_option: by default each command registers a ``--help``
                        option.  This can be disabled by this parameter.
:param no_args_is_help: this controls what happens if no arguments are
                        provided.  This option is disabled by default.
                        If enabled this will add ``--help`` as argument
                        if no arguments are passed
:param hidden: hide this command from help outputs.

:param deprecated: issues a message indicating that
                         the command is deprecated.

.. versionchanged:: 8.1
    ``help``, ``epilog``, and ``short_help`` are stored unprocessed,
    all formatting is done when outputting help text, not at init,
    and is done even if not using the ``@command`` decorator.

.. versionchanged:: 8.0
    Added a ``repr`` showing the command name.

.. versionchanged:: 7.1
    Added the ``no_args_is_help`` parameter.

.. versionchanged:: 2.0
    Added the ``context_settings`` parameter.

    
<h3><b><i><a href="#class-Command-mro" id="class-Command-mro">Ancestors (in MRO)</a></i></b></h3>

* click.core.Command
* click.core.BaseCommand

    
<h3><b><i><a href="#class-Command-func" id="class-Command-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-Command-func-get_help_option" id="class-Command-func-get_help_option">get_help_option</a></h3>

```python
(self, ctx: click.core.Context) ‑> Optional[click.core.Option]
```

    
Returns the help option object.

    
<h3><b><a href="#class-Group" id="class-Group">Group</a></b></h3>

```python
(name: str | None = None, commands: Union[Dict[str, click.core.Command], Sequence[click.core.Command], ForwardRef(None)] = None, **attrs: Any)
```

    
A group allows a command to have subcommands attached. This is
the most common way to implement nesting in Click.

:param name: The name of the group command.
:param commands: A dict mapping names to :class:`Command` objects.
    Can also be a list of :class:`Command`, which will use
    :attr:`Command.name` to create the dict.
:param attrs: Other command arguments described in
    :class:`MultiCommand`, :class:`Command`, and
    :class:`BaseCommand`.

.. versionchanged:: 8.0
    The ``commmands`` argument can be a list of command objects.

    
<h3><b><i><a href="#class-Group-mro" id="class-Group-mro">Ancestors (in MRO)</a></i></b></h3>

* click.core.Group
* click.core.MultiCommand
* click.core.Command
* click.core.BaseCommand

    
<h3><b><i><a href="#class-Group-func" id="class-Group-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-Group-func-command" id="class-Group-func-command">command</a></h3>

```python
(self, *args: Any, **kwargs: Any) ‑> Union[Callable[[Callable[..., Any]], src.utils.base_cli.Command], src.utils.base_cli.Command]
```

    
A shortcut decorator for declaring and attaching a command to
the group. This takes the same arguments as :func:`command` and
immediately registers the created command with this group by
calling :meth:`add_command`.

To customize the command class used, set the
:attr:`command_class` attribute.

.. versionchanged:: 8.1
    This decorator can be applied without parentheses.

.. versionchanged:: 8.0
    Added the :attr:`command_class` attribute.

    
<h3><b><a href="#class-cao" id="class-cao">cao</a></b></h3>

```python
(group: src.utils.base_cli.Group)
```

    
Returns wrappers for a click command evaluated from the given arguments.

    
<h3><b><i><a href="#class-cao-args" id="class-cao-args">Args:</a></i></b></h3>

- group (`Group`): Command group of the command to be under.

    
<h3><b><i><a href="#class-cao-func" id="class-cao-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-cao-func-arguments" id="class-cao-func-arguments">arguments</a></h3>

```python
(self) ‑> Callable[[Callable[..., Any]], Callable[..., Any]]
```

    
The arguments wrapper.

    
<h3><i><a href="#class-cao-func-arguments-returns" id="class-cao-func-arguments-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-cao-func-command" id="class-cao-func-command">command</a></h3>

```python
(self) ‑> Callable[[Callable[..., Any]], Callable[..., Any]]
```

    
The command wrapper.

    
<h3><i><a href="#class-cao-func-command-returns" id="class-cao-func-command-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-cao-func-kwargs_preprocessor" id="class-cao-func-kwargs_preprocessor">kwargs_preprocessor</a></h3>

```python
(self, func: Callable[..., Any]) ‑> Callable[..., Any]
```

    

    

    
<h3><a href="#class-cao-func-option_the" id="class-cao-func-option_the">option_the</a></h3>

```python
(self, maxlen_type_string: int, maxlen_opts_help: int) ‑> Callable[..., tuple[str, str, str]]
```

    

    

    
<h3><a href="#class-cao-func-options" id="class-cao-func-options">options</a></h3>

```python
(self) ‑> Callable[[Callable[..., Any]], Callable[..., Any]]
```

    
The options wrapper.
My God in heaven, I'm agnostic, but please save me from all evil. Amen.

    
<h3><i><a href="#class-cao-func-options-returns" id="class-cao-func-options-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-cao-func-wrap" id="class-cao-func-wrap">wrap</a></h3>

```python
(self, func: Callable[..., Any]) ‑> Callable[..., Any]
```

    

    
<h3><i><a href="#class-cao-func-wrap-args" id="class-cao-func-wrap-args">Args:</a></i></h3>

- func (`Callable[..., Any]`): Function to be wrapped.

    
<h3><i><a href="#class-cao-func-wrap-returns" id="class-cao-func-wrap-returns">Returns:</a></i></h3>

`Callable[..., Any]`: Wrapped function.