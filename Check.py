from typing import TypeVar

from Permission import Permission

from MetaCheck import MetaCheck


T = TypeVar("T")


class Check(MetaCheck):
    def __init__(self, permission: Permission, permission_name: str = "permissions") -> None:
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

        super().__init__(check_permission)

    @classmethod
    def from_int(cls, permission: int, permission_name: str = "permissions"):
        return cls(Permission(permission), permission_name)
