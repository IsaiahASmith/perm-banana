from MetaCheck import MetaCheck
from Permission import Permission
from banana import banana


def test_init():
    @banana
    class Test:
        def __init__(self, test):
            self.test = test

    test = Test(0)
    assert test.test == 0


def test_inside_class():
    class Test:
        test = MetaCheck(lambda *_: True)

        def __init__(self, test):
            self.test2 = test

    test = Test(0)
    assert test.test2 == 0
    assert test.test


def test_inside_from_int():
    @banana
    class Test:
        test: int = 0b1100

        def __init__(self, perms):
            self.permissions = perms

    test = Test(Permission(0))
    assert not test.test
    test.permissions = Permission(0b1100)
    assert test.test


def test_inside_instance():
    class Test:
        test = MetaCheck(lambda self: getattr(self, "test2"))

        def __init__(self, test):
            self.test2 = test

    test = Test(True)
    test2 = Test(False)
    assert test.test2
    assert test.test
    assert not test2.test2
    assert not test2.test


def test_updates_dynamically():
    class Test:
        test = MetaCheck(lambda self: getattr(self, "test2"))

        def __init__(self, test):
            self.test2 = test

    test = Test(True)
    test.test2 = False
    assert not test.test
