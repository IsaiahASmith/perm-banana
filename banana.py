from typing import Optional

from Check import Check


def get_check(cls, name) -> Optional[Check]:
    """
    Gets the class variables and converts them to a check if they are not already.
    """
    default = getattr(cls, name, None)
    if isinstance(default, Check):
        check = default
    elif isinstance(default, int):
        check = Check.from_int(permission=default)
    else:
        return None
    return check


def banana(cls):
    cls_annotations = cls.__dict__.get("__annotations__", {})
    for name in cls_annotations.keys():
        check = get_check(cls, name)
        if check is None:
            continue
        setattr(cls, name, check)
    return cls
