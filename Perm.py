from dataclasses import dataclass

from Check import Check


@dataclass(unsafe_hash=True)
class Perm:
    name: str
    check: Check
