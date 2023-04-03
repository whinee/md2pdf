"""`Common` exceptions are raised if an error occured and it is of the `Common` exception's common variant of error."""

from typing import Any, Optional

try:
    from utils.base_exc import c_exc, c_exc_str

    from ..globals import LANG_C
    from ..info import PLATFORM, PSH, TW
except ImportError:
    from src.globals import LANG_C
    from src.info import PLATFORM, PSH, TW
    from src.utils.base_exc import c_exc, c_exc_str


class GeneralExceptions:
    class ValidationError:
        @c_exc_str
        class FileNotFound(FileNotFoundError):
            def __init__(self, fp: str) -> None:
                """
                Raised when a file in a given path is not found.

                Args:
                - parameter (`fp`): Path of the file that can not be found.
                """
                self.message = f"`{fp}` does not exist."

        @c_exc_str
        class Arguments:
            def __init__(
                self,
                parameter: str,
                argument: Any,
                specification: str,
            ) -> None:
                """
                Raised when a parameter is required to be of specification, but is not followed.

                Args:
                - parameter (`str`): Name of the parameter.
                - argument (`any`): Argument passed to the parameter.
                - specification (`str`): Specification/s of the parameter.
                """
                self.message = f"Argument `{parameter}` needs to {specification}. Instead, passed in the following: {argument}"

        @c_exc
        class Common(Exception):
            pass

    @c_exc_str
    class PrerequisiteNotFound:
        def __init__(
            self,
            prerequisite: str,
            inst_instruction: Optional[str] = None,
        ) -> None:
            """
            Raised when a prerequisite is needed by the program, but is not installed in the machine.

            Args:
            - prerequisite (`str`): Name of the prerequisite.
            - inst_instruction (`Optional[str]`, optional): Instructions for installing the prerequisite. Defaults to `None`.
            """
            self.message = f"prerequisite `{prerequisite}` cannot be found."


class CLIExceptions:
    @c_exc_str
    class TerminalTooThin(Exception):
        def __init__(self, min_width: int) -> None:
            """
            Raised when terminal is too thin for content to be rendered.

            Args:
            - min_width (`int`): Required minimum terminal width.
            """
            self.message = f"Please widen terminal.\nCurrent Width: {TW}\nMinimum Width: {min_width}"

    class ValidationError:
        @c_exc_str
        class OptionRequired(Exception):
            def __init__(self, option: str) -> None:
                """
                Raised when an option is required but no argument is passed.

                Args:
                - option (`str`): Required option with no arguments passed into it.
                """
                self.message = f"Option `{option}` is required."

        @c_exc
        class Common(Exception):
            pass


class CDExceptions:
    class API:
        @c_exc
        class KeyError(KeyError):  # type: ignore[misc]
            pass

        @c_exc_str
        class KeyNotInElement(KeyError):
            def __init__(self, key: str) -> None:
                self.message = f"`{key}` not in element"

        @c_exc
        class TypeError(TypeError):  # type: ignore[misc]
            pass

        @c_exc_str
        class IndexError(IndexError):  # type: ignore[misc]
            def __init__(
                self,
                sep: str,
                og_path: str,
                idx: int,
                ls_idx: int,
                len_iter: int,
            ) -> None:
                self.message = "sized iterable index out of range"
                self.details = f"""`{sep.join(og_path.split(sep)[:idx])}`:
                Index is `{ls_idx}` while the length of the sized iterable is only `{len_iter}`.
                The index should fulfill the following condition:
                (len(iter)) > idx > (-1 - len(iter))

                The index should be less than the length of the sized iterable AND or more than the difference of negative 1 and the length of the sized iterable."""

    class Internals:
        class StateUnexpected(IndexError):
            def __init__(self, state: Any, max_state: int) -> None:
                """
                Raised when the state passed in between functions is not of type `int` or exceeds the bounds of possible states.

                Args:
                - state (`Any`): Faulty state.
                - max_state (`Optional[str]`): Maximum integer for state.
                """
                self.message = "state index out of range"
                self.details = f"""Passed state is `{state}` while the max integer for state is `{max_state}`.
                The index should fulfill the following condition:
                - State should be an integer
                - State should be more than `-1` or less than `{max_state + 1}`"""


class KatexExceptions:
    @c_exc_str
    class NotFound(Exception):
        def __init__(self) -> None:
            """Raised when the packaged KaTeX binaries are not compatible for the machine's platform, and a local KaTeX installation can not be found."""
            self.message = LANG_C.dir("cli/katex/not_installed_msg")
            if PSH in ["win", "mac", "linux"]:
                self.details = LANG_C.dir("cli/katex/not_installed_tpl").format(
                    platform=PLATFORM,
                    instruction=LANG_C.dir(f"cli/katex/not_installed_{PSH}"),
                )
            else:
                self.details = LANG_C.dir("cli/katex/not_installed_no_solution")
