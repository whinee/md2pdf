from typing import Any, Callable, Iterable, Sequence, TypeAlias

Args: TypeAlias = list[Any]
CallableAny: TypeAlias = Callable[..., Any]
CallableAnyAny: TypeAlias = Callable[[Any], Any]
IterAny: TypeAlias = Iterable[Any]
IterIterAny: TypeAlias = Iterable[Iterable[Any]]
Kwargs: TypeAlias = dict[str, Any]
ListAny: TypeAlias = Args
SequenceAny: TypeAlias = Sequence[Any]
TupleAny: TypeAlias = tuple[None] | tuple[Any] | tuple[Any, ...]
TupleStr: TypeAlias = tuple[str] | tuple[str, ...]
