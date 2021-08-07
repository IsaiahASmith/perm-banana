from typing import Set

from Perm import Perm


def banana(perms: Set[Perm]):
    def peal_class(cls):
        for perm in perms:
            setattr(cls, perm.name, perm.check)
        return cls

    return peal_class
