from typing import TypeVar, Callable, Any, Optional


T = TypeVar("T")
V = TypeVar("V")


class Check(object):
    def __init__(self, fget: Callable[[Any], V], doc: str = "") -> None:
        self.fget = fget
        if doc is None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj: Optional[T], type: Optional[T]) -> V:
        if obj is None:
            return self
        return self.fget(obj)
