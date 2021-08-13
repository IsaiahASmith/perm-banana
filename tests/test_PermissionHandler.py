from Permission import Permission
from PermissionHandler import PermissionHandler


def test_initialization():
    permission = Permission(0)
    PermissionHandler(permission)


def test_bool():
    permission = Permission(0)
    assert not bool(PermissionHandler(permission))
    permission1 = Permission(1)
    assert bool(PermissionHandler(permission1))
    assert not bool(PermissionHandler(permission, {1: PermissionHandler(permission), 2: PermissionHandler(permission)}))
    assert bool(PermissionHandler(permission, {1: PermissionHandler(permission1), 2: PermissionHandler(permission)}))


def test_invert():
    old_handler = PermissionHandler(Permission(0b0011), {1: PermissionHandler(Permission(0b0011))})
    handler = ~old_handler
    assert Permission(0b0011) == old_handler.permission
    assert ~Permission(0b0011) == handler.permission
    assert Permission(0b0011) == old_handler.children[1].permission
    assert ~Permission(0b0011) == handler.children[1].permission


def test_and():
    handler_left = PermissionHandler(Permission(0b1110), {1: PermissionHandler(Permission(0b1110))})
    handler_right = PermissionHandler(Permission(0b0111), {1: PermissionHandler(Permission(0b0111))})
    handler_and = handler_left & handler_right
    assert Permission(0b1110) == handler_left.permission
    assert Permission(0b0111) == handler_right.permission
    assert Permission(0b0110) == handler_and.permission
    assert Permission(0b1110) == handler_left.children[1].permission
    assert Permission(0b0111) == handler_right.children[1].permission
    assert Permission(0b0110) == handler_and.children[1].permission


def test_and_mismatch():
    handler_left = PermissionHandler(Permission(0b1110), {1: PermissionHandler(Permission(0b1110))})
    handler_right = PermissionHandler(Permission(0b0111), {2: PermissionHandler(Permission(0b0111))})
    handler_and = handler_left & handler_right
    assert Permission(0b1110) == handler_left.children[1].permission
    assert 2 not in handler_left.children
    assert Permission(0b0111) == handler_right.children[2].permission
    assert 1 not in handler_right.children
    assert 1 not in handler_and.children
    assert 2 not in handler_and.children


def test_iand():
    handler_left = PermissionHandler(Permission(0b1110), {1: PermissionHandler(Permission(0b1110))})
    handler_right = PermissionHandler(Permission(0b0111), {1: PermissionHandler(Permission(0b0111))})
    handler_left &= handler_right
    assert Permission(0b0110) == handler_left.permission
    assert Permission(0b0111) == handler_right.permission
    assert Permission(0b0110) == handler_left.children[1].permission
    assert Permission(0b0111) == handler_right.children[1].permission


def test_iand_mismatch():
    handler_left = PermissionHandler(Permission(0b1110), {2: PermissionHandler(Permission(0b1110))})
    handler_right = PermissionHandler(Permission(0b0111), {1: PermissionHandler(Permission(0b0111))})
    handler_left &= handler_right
    assert Permission(0b0110) == handler_left.permission
    assert Permission(0b0111) == handler_right.permission
    assert 1 not in handler_left.children
    assert 2 not in handler_left.children
    assert Permission(0b0111) == handler_right.children[1].permission


def test_or():
    handler_left = PermissionHandler(Permission(0b1000), {1: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_and = handler_left | handler_right
    assert Permission(0b1000) == handler_left.permission
    assert Permission(0b0001) == handler_right.permission
    assert Permission(0b1001) == handler_and.permission
    assert Permission(0b1000) == handler_left.children[1].permission
    assert Permission(0b0001) == handler_right.children[1].permission
    assert Permission(0b1001) == handler_and.children[1].permission


def test_or_mismatch():
    handler_left = PermissionHandler(Permission(0b1000), {2: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_and = handler_left | handler_right
    assert Permission(0b1000) == handler_left.children[2].permission
    assert Permission(0b0001) == handler_right.children[1].permission
    assert Permission(0b0001) == handler_and.children[1].permission
    assert Permission(0b1000) == handler_and.children[2].permission


def test_ior():
    handler_left = PermissionHandler(Permission(0b1000), {1: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_left |= handler_right
    assert Permission(0b1001) == handler_left.permission
    assert Permission(0b0001) == handler_right.permission
    assert Permission(0b1001) == handler_left.children[1].permission
    assert Permission(0b0001) == handler_right.children[1].permission


def test_ior_mismatch():
    handler_left = PermissionHandler(Permission(0b1000), {2: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_left |= handler_right
    assert Permission(0b0001) == handler_left.children[1].permission
    assert Permission(0b1000) == handler_left.children[2].permission


def test_add():
    handler_left = PermissionHandler(Permission(0b1000), {1: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_and = handler_left + handler_right
    assert Permission(0b1000) == handler_left.permission
    assert Permission(0b0001) == handler_right.permission
    assert Permission(0b1001) == handler_and.permission
    assert Permission(0b1000) == handler_left.children[1].permission
    assert Permission(0b0001) == handler_right.children[1].permission
    assert Permission(0b1001) == handler_and.children[1].permission


def test_add_mismatch():
    handler_left = PermissionHandler(Permission(0b1000), {2: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_and = handler_left + handler_right
    assert Permission(0b1000) == handler_left.children[2].permission
    assert Permission(0b0001) == handler_right.children[1].permission
    assert Permission(0b0001) == handler_and.children[1].permission
    assert Permission(0b1000) == handler_and.children[2].permission


def test_iadd():
    handler_left = PermissionHandler(Permission(0b1000), {1: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_left += handler_right
    assert Permission(0b1001) == handler_left.permission
    assert Permission(0b0001) == handler_right.permission
    assert Permission(0b1001) == handler_left.children[1].permission
    assert Permission(0b0001) == handler_right.children[1].permission


def test_iadd_mismatch():
    handler_left = PermissionHandler(Permission(0b1000), {2: PermissionHandler(Permission(0b1000))})
    handler_right = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler_left += handler_right
    assert Permission(0b0001) == handler_left.children[1].permission
    assert Permission(0b1000) == handler_left.children[2].permission


def test_sub():
    handler_left = PermissionHandler(Permission(0b1010), {1: PermissionHandler(Permission(0b1010))})
    handler_right = PermissionHandler(Permission(0b1100), {1: PermissionHandler(Permission(0b1100))})
    handler_sub = handler_left - handler_right
    assert Permission(0b1010) == handler_left.permission
    assert Permission(0b1100) == handler_right.permission
    assert Permission(0b0010) == handler_sub.permission
    assert Permission(0b1010) == handler_left.children[1].permission
    assert Permission(0b1100) == handler_right.children[1].permission
    assert Permission(0b0010) == handler_sub.children[1].permission


def test_sub_mismatch():
    handler_left = PermissionHandler(Permission(0b1010), {2: PermissionHandler(Permission(0b1010))})
    handler_right = PermissionHandler(Permission(0b1100), {1: PermissionHandler(Permission(0b1100))})
    handler_sub = handler_left - handler_right
    assert Permission(0b1010) == handler_left.children[2].permission
    assert Permission(0b1100) == handler_right.children[1].permission
    assert 1 not in handler_sub.children
    assert Permission(0b1010) == handler_sub.children[2].permission


def test_isub():
    handler_left = PermissionHandler(Permission(0b1110), {1: PermissionHandler(Permission(0b1110))})
    handler_right = PermissionHandler(Permission(0b1101), {1: PermissionHandler(Permission(0b1101))})
    handler_left -= handler_right
    assert Permission(0b0010) == handler_left.permission
    assert Permission(0b1101) == handler_right.permission
    assert Permission(0b0010) == handler_left.children[1].permission
    assert Permission(0b1101) == handler_right.children[1].permission


def test_isub_mismatch():
    handler_left = PermissionHandler(Permission(0b1010), {2: PermissionHandler(Permission(0b1010))})
    handler_right = PermissionHandler(Permission(0b1100), {1: PermissionHandler(Permission(0b1100))})
    handler_left -= handler_right
    assert 1 not in handler_left.children
    assert Permission(0b1010) == handler_left.children[2].permission


def test_eq():
    handler1 = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler2 = PermissionHandler(Permission(0b1111), {1: PermissionHandler(Permission(0b1111))})
    assert not handler2 == handler1
    assert not handler1 == handler2
    assert handler1 == handler1
    assert handler2 == handler2


def test_eq_mismatch():
    handler1 = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler2 = PermissionHandler(
        Permission(0b0001), {1: PermissionHandler(Permission(0b0001)), 2: PermissionHandler(Permission(0b1111))}
    )
    assert not handler1 == handler2
    assert not handler2 == handler1


def test_ne():
    handler1 = PermissionHandler(Permission(0b0001), {1: PermissionHandler(Permission(0b0001))})
    handler2 = PermissionHandler(Permission(0b1111), {1: PermissionHandler(Permission(0b1111))})
    assert handler2 != handler1
    assert handler1 != handler2
    assert not handler1 != handler1
    assert not handler2 != handler2
