from typing import Dict, Union

from .Permission import Permission


class PermissionHandler:
    """Finds the given permissions of a user and contains them for their respective"""

    def __init__(self, permission: Permission, children: Dict[int, "PermissionHandler"]):
        self.permission = permission
        self.children = children

    @property
    def permissions(self) -> Dict[int, Union["PermissionHandler", Permission]]:
        """Finds all valid permission of itself and its children"""
        return {0: self.permission, **self.children}

    def __bool__(self) -> bool:
        return all(bool(permission) for permission in self.permissions.values())

    def __invert__(self):
        self.permission = ~self.permission
        temp_children = {}

        for key, child in self.children.items():
            temp_children[key] = ~child

        self.children = temp_children

    def __and__(self, other):
        children_keys = set(self.children.keys()).intersection(other.children.keys())

        return PermissionHandler(
            self.permission & other.permissions,
            {key: self.children[key] & other.children[key] for key in children_keys},
        )

    def __iand__(self, other):
        children_keys = set(self.children.keys()).intersection(other.children.keys())

        self.permission &= other.permissions
        for key in children_keys:
            self.children[key] &= other.children[key]

        return self

    def __or__(self, other):
        children = {}
        both = {*self.children.keys(), *other.children.keys()}
        for key in both:
            if key in self.children and key in other.children:
                children.update({key: self.children[key] | other.children[key]})
            elif key in self.children:
                children.update({key: self.children[key]})
            else:
                children.update({key: other.children[key]})

        return PermissionHandler(self.permission | other.permissions, children)

    def __ior__(self, other):
        self.permission |= other.permission
        self.children
        return self

    def __add__(self, other):
        return self | other

    def __iadd__(self, other):
        self |= other
        return self

    def __sub__(self, other):
        return self & ~other

    def __isub__(self, other):
        self &= ~other
        return self

    def __eq__(self, other):
        if not self.permissions == other.permissions:
            return False
        for key in self.children.keys():
            if key not in other.children or self.children[key] != other.children[key]:
                return False
        return True

    def __ne__(self, other):
        return not self == other
