# **[src](../index.md).[utils](../utils.md).[base_cli](base_cli.md)**

    
Hereunder resides functions for constructing CLI for this program.

> This module heavily documents my descent to madness.
>
> An unholy amalgamation of megalamonia, depression, God complex, and impostor syndrome filled my broken heart.
>
> This file is the digital manifestation of my mental woes.
>
> Masochistic tendencies fuelling my coding sessions.
>
> I wish upon this abyss to not touch this file ever again.

whi~nyaan! ― 2023

    
<h2><b><a href="#func" id="func">Functions</a></b></h2>

    

    
<h3><b><a href="#func-command" id="func-command">command</a></b></h3>

```python
(group: src.utils.base_cli.Group) ‑> collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], collections.abc.Callable[..., typing.Any]]
```

    
Wrapper for click commands.

    
<h3><b><i><a href="#func-command-args" id="func-command-args">Args:</a></i></b></h3>

- group (`Group`): Command group of the command to be under.

    
<h3><b><i><a href="#func-command-returns" id="func-command-returns">Returns:</a></i></b></h3>

- `Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><b><a href="#func-command_group" id="func-command_group">command_group</a></b></h3>

```python
(name: str | collections.abc.Callable[..., typing.Any] | None = None, **attrs: Any) ‑> src.utils.base_cli.Group
```

    

    

    
<h3><b><a href="#func-custom_command" id="func-custom_command">custom_command</a></b></h3>

```python
(name: str | collections.abc.Callable[..., typing.Any] | None = None, cls: Optional[type[src.utils.base_cli.Command]] = None, **attrs: Any) ‑> src.utils.base_cli.Command | collections.abc.Callable[..., src.utils.base_cli.Command]
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
(message: str, choices: collections.abc.Sequence[str | questionary.prompts.common.Choice | dict[str, typing.Any]] | dict[str, typing.Any], default: Optional[Any] = None, instruction: str | None = None, qmark: str | None = None, pointer: str | None = None, style: Optional[prompt_toolkit.styles.base.BaseStyle] = None, show_selected: bool | None = None, ret_err: bool | None = None, **kwargs: dict[str, typing.Any]) ‑> tuple[bool, typing.Any]
```

    

    

    
<h3><b><a href="#func-show_help" id="func-show_help">show_help</a></b></h3>

```python
(ctx: click.core.Context, param: click.core.Parameter, value: str) ‑> None
```

    

    
<h2><b><a href="#class" id="class">Classes</a></b></h2>

    
<h3><b><a href="#class-CAO" id="class-CAO">CAO</a></b></h3>

```python
(group: src.utils.base_cli.Group)
```

    
Returns wrappers for a click command evaluated from the given arguments.

Initialize object.

    
<h3><b><i><a href="#class-CAO-args" id="class-CAO-args">Args:</a></i></b></h3>

- group (`Group`): Command group of the command to be under.

    
<h3><b><i><a href="#class-CAO-func" id="class-CAO-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-CAO-func-arguments" id="class-CAO-func-arguments">arguments</a></h3>

```python
(self) ‑> collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], collections.abc.Callable[..., typing.Any]]
```

    
The arguments wrapper.

    
<h3><i><a href="#class-CAO-func-arguments-returns" id="class-CAO-func-arguments-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-CAO-func-command" id="class-CAO-func-command">command</a></h3>

```python
(self) ‑> collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], collections.abc.Callable[..., typing.Any]]
```

    
The command wrapper.

    
<h3><i><a href="#class-CAO-func-command-returns" id="class-CAO-func-command-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-CAO-func-kwargs_preprocessor" id="class-CAO-func-kwargs_preprocessor">kwargs_preprocessor</a></h3>

```python
(self, func: collections.abc.Callable[..., typing.Any]) ‑> collections.abc.Callable[..., typing.Any]
```

    

    

    
<h3><a href="#class-CAO-func-option_the" id="class-CAO-func-option_the">option_the</a></h3>

```python
(self, maxlen_type_string: int, maxlen_opts_help: int) ‑> collections.abc.Callable[..., tuple[str, str, str]]
```

    

    

    
<h3><a href="#class-CAO-func-options" id="class-CAO-func-options">options</a></h3>

```python
(self) ‑> collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], collections.abc.Callable[..., typing.Any]]
```

    
The options wrapper.

My God in heaven, I'm agnostic, but please save me from all evil. Amen.

    
<h3><i><a href="#class-CAO-func-options-returns" id="class-CAO-func-options-returns">Returns:</a></i></h3>

`Callable[[Callable[..., Any]], Callable[..., Any]]`

    

    
<h3><a href="#class-CAO-func-wrap" id="class-CAO-func-wrap">wrap</a></h3>

```python
(self, func: collections.abc.Callable[..., typing.Any]) ‑> collections.abc.Callable[..., typing.Any]
```

    
Wrap given function with corresponding click decorators.

    
<h3><i><a href="#class-CAO-func-wrap-args" id="class-CAO-func-wrap-args">Args:</a></i></h3>

- func (`Callable[..., Any]`): Function to be wrapped.

    
<h3><i><a href="#class-CAO-func-wrap-returns" id="class-CAO-func-wrap-returns">Returns:</a></i></h3>

`Callable[..., Any]`: Wrapped function.

    
<h3><b><a href="#class-Command" id="class-Command">Command</a></b></h3>

```python
(name: str | None, context_settings: Optional[dict[str, typing.Any]] = None, callback: Optional[collections.abc.Callable[..., typing.Any]] = None, params: Optional[list[click.core.Parameter]] = None, help: str | None = None, epilog: str | None = None, short_help: str | None = None, options_metavar: str | None = '[OPTIONS]', add_help_option: bool = True, no_args_is_help: bool = False, hidden: bool = False, deprecated: bool = False)
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

    
<h3><b><i><a href="#class-Command-sub" id="class-Command-sub">Descendants</a></i></b></h3>

* src.utils.base_cli.MultiCommand

    
<h3><b><i><a href="#class-Command-var" id="class-Command-var">Instance variables</a></i></b></h3>

    
`callback`
the callback to execute when the command fires.  This might be
`None` in which case nothing happens.

    
`name`
the list of parameters for this command in the order they
should show up in the help page and execute.  Eager parameters
will automatically be handled before non eager ones.

    
<h3><b><i><a href="#class-Command-func" id="class-Command-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-Command-func-format_usage" id="class-Command-func-format_usage">format_usage</a></h3>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) ‑> None
```

    
Writes the usage line into the formatter.

This is a low-level method called by :meth:`get_usage`.

    

    
<h3><a href="#class-Command-func-get_help_option" id="class-Command-func-get_help_option">get_help_option</a></h3>

```python
(self, ctx: click.core.Context) ‑> Optional[click.core.Option]
```

    
Returns the help option object.

    
<h3><b><a href="#class-Group" id="class-Group">Group</a></b></h3>

```python
(name: str | None = None, commands: Union[dict[str, src.utils.base_cli.Command], collections.abc.Sequence[src.utils.base_cli.Command], ForwardRef(None)] = None, **attrs: Any)
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

    
<h3><b><i><a href="#class-Group-mro" id="class-Group-mro">Ancestors (in MRO)</a></i></b></h3>

* src.utils.base_cli.MultiCommand
* src.utils.base_cli.Command
* click.core.Command
* click.core.BaseCommand

    
<h3><b><i><a href="#class-Group-cvar" id="class-Group-cvar">Class variables</a></i></b></h3>

    
`command_class: Optional[type[src.utils.base_cli.Command]]`

    
`group_class: Union[type['Group'], type[type], ForwardRef(None)]`

    
<h3><b><i><a href="#class-Group-var" id="class-Group-var">Instance variables</a></i></b></h3>

    
`commands`
The registered subcommands by their exported names.

    
<h3><b><i><a href="#class-Group-func" id="class-Group-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-Group-func-add_command" id="class-Group-func-add_command">add_command</a></h3>

```python
(self, cmd: src.utils.base_cli.Command, name: str | None = None) ‑> None
```

    

    

    
<h3><a href="#class-Group-func-command" id="class-Group-func-command">command</a></h3>

```python
(self, *args: Any, **kwargs: Any) ‑> collections.abc.Callable[[collections.abc.Callable[..., typing.Any]], src.utils.base_cli.Command] | src.utils.base_cli.Command
```

    

    

    
<h3><a href="#class-Group-func-get_command" id="class-Group-func-get_command">get_command</a></h3>

```python
(self, ctx: click.core.Context, cmd_name: str) ‑> Optional[src.utils.base_cli.Command]
```

    

    

    
<h3><a href="#class-Group-func-group" id="class-Group-func-group">group</a></h3>

```python
(self, *args: Any, **kwargs: Any) ‑> Union[collections.abc.Callable[[collections.abc.Callable[..., Any]], 'Group'], src.utils.base_cli.Group]
```

    

    

    
<h3><a href="#class-Group-func-list_commands" id="class-Group-func-list_commands">list_commands</a></h3>

```python
(self, ctx: click.core.Context) ‑> list[str]
```

    

    
<h3><b><a href="#class-MultiCommand" id="class-MultiCommand">MultiCommand</a></b></h3>

```python
(name: str | None = None, invoke_without_command: bool = False, no_args_is_help: bool | None = None, subcommand_metavar: str | None = None, chain: bool = False, result_callback: Optional[collections.abc.Callable[..., typing.Any]] = None, **attrs: Any)
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

    
<h3><b><i><a href="#class-MultiCommand-mro" id="class-MultiCommand-mro">Ancestors (in MRO)</a></i></b></h3>

* src.utils.base_cli.Command
* click.core.Command
* click.core.BaseCommand

    
<h3><b><i><a href="#class-MultiCommand-sub" id="class-MultiCommand-sub">Descendants</a></i></b></h3>

* src.utils.base_cli.Group

    
<h3><b><i><a href="#class-MultiCommand-cvar" id="class-MultiCommand-cvar">Class variables</a></i></b></h3>

    
`allow_extra_args`

    
`allow_interspersed_args`

    
<h3><b><i><a href="#class-MultiCommand-func" id="class-MultiCommand-func">Methods</a></i></b></h3>

    

    
<h3><a href="#class-MultiCommand-func-collect_usage_pieces" id="class-MultiCommand-func-collect_usage_pieces">collect_usage_pieces</a></h3>

```python
(self, ctx: click.core.Context) ‑> list[str]
```

    
Returns all the pieces that go into the usage line and returns
it as a list of strings.

    

    
<h3><a href="#class-MultiCommand-func-format_commands" id="class-MultiCommand-func-format_commands">format_commands</a></h3>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) ‑> None
```

    

    

    
<h3><a href="#class-MultiCommand-func-format_options" id="class-MultiCommand-func-format_options">format_options</a></h3>

```python
(self, ctx: click.core.Context, formatter: click.formatting.HelpFormatter) ‑> None
```

    
Writes all the options into the formatter if they exist.

    

    
<h3><a href="#class-MultiCommand-func-get_command" id="class-MultiCommand-func-get_command">get_command</a></h3>

```python
(self, ctx: click.core.Context, cmd_name: str) ‑> Optional[src.utils.base_cli.Command]
```

    

    

    
<h3><a href="#class-MultiCommand-func-invoke" id="class-MultiCommand-func-invoke">invoke</a></h3>

```python
(self, ctx: click.core.Context) ‑> Any
```

    
Given a context, this invokes the attached callback (if it exists)
in the right way.

    

    
<h3><a href="#class-MultiCommand-func-list_commands" id="class-MultiCommand-func-list_commands">list_commands</a></h3>

```python
(self, ctx: click.core.Context) ‑> list[str]
```

    

    

    
<h3><a href="#class-MultiCommand-func-parse_args" id="class-MultiCommand-func-parse_args">parse_args</a></h3>

```python
(self, ctx: click.core.Context, args: list[str]) ‑> list[str]
```

    
Given a context and a list of arguments this creates the parser
and parses the arguments, then modifies the context as necessary.
This is automatically invoked by :meth:`make_context`.

    

    
<h3><a href="#class-MultiCommand-func-resolve_command" id="class-MultiCommand-func-resolve_command">resolve_command</a></h3>

```python
(self, ctx: click.core.Context, args: list[str]) ‑> tuple[typing.Optional[str], typing.Optional[src.utils.base_cli.Command], list[str]]
```

    

    

    
<h3><a href="#class-MultiCommand-func-result_callback" id="class-MultiCommand-func-result_callback">result_callback</a></h3>

```python
(self, replace: bool = False) ‑> collections.abc.Callable[[~F], ~F]
```

    

    

    
<h3><a href="#class-MultiCommand-func-shell_complete" id="class-MultiCommand-func-shell_complete">shell_complete</a></h3>

```python
(self, ctx: click.core.Context, incomplete: str)
```

    
Return a list of completions for the incomplete value. Looks
at the names of options and chained multi-commands.

:param ctx: Invocation context for this command.
:param incomplete: Value being completed. May be empty.

.. versionadded:: 8.0

    

    
<h3><a href="#class-MultiCommand-func-to_info_dict" id="class-MultiCommand-func-to_info_dict">to_info_dict</a></h3>

```python
(self, ctx: click.core.Context) ‑> dict[str, typing.Any]
```

    
Gather information that could be useful for a tool generating
user-facing documentation. This traverses the entire structure
below this command.

Use :meth:`click.Context.to_info_dict` to traverse the entire
CLI structure.

:param ctx: A :class:`Context` representing this command.

.. versionadded:: 8.0