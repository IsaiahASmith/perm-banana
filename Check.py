from typing import Callable, Any, Optional

from Permission import Permission


class Check(object):
    fget: Callable[[Permission], bool]

    def __init__(self, fget: Callable[[Any], Any], doc: str = ""):
        self.fget = fget
        if doc is None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj: Permission, type: Optional[type]) -> bool:
        return self.fget(obj)
