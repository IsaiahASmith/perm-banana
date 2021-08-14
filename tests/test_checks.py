from perm_banana.Check import Check
from perm_banana.Permission import Permission
from perm_banana.PermissionHandler import PermissionHandler


def test_check_initialization():
    Check(Permission(0b0011))
    Check(PermissionHandler(Permission(0b0011)))


def test_check_from_int():
    Check.from_int(0b0001)


def test_check_valid_permission():
    class Test:
        test = Check(Permission(1))

        def __init__(self, perms: Permission):
            self.permissions = perms

    test = Test(Permission(0))
    assert not test.test
    test.permissions = Permission(1)
    assert test.test


def test_check_valid_handler():
    class Test:
        test = Check(PermissionHandler(Permission(1), {1: PermissionHandler(Permission(1))}))

        def __init__(self, perms: PermissionHandler):
            self.permissions = perms

    test = Test(PermissionHandler(Permission(0)))
    assert not test.test
    test.permissions = PermissionHandler(Permission(1), {1: PermissionHandler(Permission(1))})
    assert test.test
