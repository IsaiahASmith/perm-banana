from Permission import Permission
from MetaCheck import MetaCheck
from NameConflictException import NameConflictException


class Check(MetaCheck):
    def __init__(self, permission: Permission, permission_name: str = "permissions") -> None:
        self._permission = permission
        self._permission_name = permission_name

        def check_permission(obj):
            """
            Checks against the permission of a class.
            If the permissions provided from the decorator are inside the current instance's
            permissions, then True will be provided, otherwise False.
            """
            current_permissions = getattr(obj, self._permission_name, None)
            if current_permissions is None:
                raise AttributeError(f"{obj} has no variable {self._permission_name} to check")
            return self._permission in current_permissions

        super().__init__(check_permission)

    def __repr__(self) -> str:
        if self._permission_name == "permissions":
            return f"{self.__class__.__name__}({self._permission})"
        else:
            return f"{self.__class__.__name__}({self._permission}, permission_name={self._permission_name})"

    def __and__(self, other):
        if self._permission_name != other._permission_name:
            raise NameConflictException(self._permission_name, other._permission_name)
        return Check(self._permission & other._permission, self._permission_name)

    def __or__(self, other):
        if self._permission_name != other._permission_name:
            raise NameConflictException(self._permission_name, other._permission_name)
        return Check(self._permission | other._permission, self._permission_name)

    @classmethod
    def from_int(cls, permission: int, permission_name: str = "permissions"):
        return cls(Permission(permission), permission_name)
