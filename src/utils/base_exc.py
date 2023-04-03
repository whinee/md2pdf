from collections.abc import Callable
from typing import Optional

try:
    from . import types
    from .style import S, pp
except ImportError:
    from src.utils import types
    from src.utils.style import S, pp


def c_exc_str(cls: type[BaseException]) -> type[BaseException]:
    """
    Decorator to add the __str__ method to an exception.

    Args:
    - cls (`BaseException`): The exception to add the __str__ method to.

    Returns:
    `BaseException`: The exception to raise.
    """

    old_init: Callable[..., None] = cls.__init__

    def init(self: BaseException, *args: types.Args, **kwargs: types.Kwargs) -> None:
        old_init(self, *args, **kwargs)
        pp(S.p_critical(S.t_critical(self.message)))
        if details := getattr(self, "details", None):
            print(details)

    def str_fn(self: BaseException) -> str:
        msg: str = self.message
        # details: str=getattr(self, 'details')
        # if details:
        #     return msg + '\n' + details
        return msg

    cls.__init__ = init  # type: ignore[assignment]
    cls.__str__ = str_fn  # type: ignore[assignment]
    return cls


def c_exc(cls: type[BaseException]) -> type[BaseException]:
    """
    Decorator to raise a custom exception.

    This function gives the class an __init__ function that raises the exception.
    If the class does not inherit from any Exception, it will be automatically inherit from Exception.
    This function also wraps the Exception with `c_exc_str` method, for adding the `__str__` method.

    Args:
    - cls (`BaseException | Object`): The exception to modify.

    Returns:
    `BaseException`: The exception to raise.
    """
    if cls.__mro__[-2] is BaseException:
        exc = cls.__mro__[1]
    else:
        exc = Exception

    def init(
        self: type[BaseException],
        message: str,
        details: Optional[str] = None,
    ) -> None:
        self.message = message
        if details is not None:
            self.details = details
        exc(self.message)

    cls.__init__ = init  # type: ignore[assignment, attr-defined, misc, no-any-return]
    return c_exc_str(cls)
