from typing import TypeVar, Union, Callable, Any, Optional

from Permission import Permission


T = TypeVar("T")


class Check(object):
    def __init__(self, fget: Callable[[Any], bool], doc: str = None) -> None:
        self.fget = fget
        if doc is None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj: Optional[T], type: Optional[T]) -> Union[bool, "Check"]:
        if obj is None:
            return self
        return self.fget(obj)

    def __set__(self, obj: Optional[T], value) -> None:
        raise AttributeError("Cannot change the value")

    @classmethod
    def from_int(cls, permission: int, permission_name: str = "permissions"):
        return cls.from_permission(Permission(permission), permission_name)

    @classmethod
    def from_permission(cls, permission: Permission, permission_name: str = "permissions"):
        def check_permission(obj):
            """
            Checks against the permission of a class.
            If the permissions provided from the decorator are inside the current instance's
            permissions, then True will be provided, otherwise False.
            """
            current_permissions = getattr(obj, permission_name, None)
            if current_permissions is None:
                raise AttributeError(f"{obj} has no variable {permission_name} to check")
            return permission in current_permissions

        return cls(check_permission)
