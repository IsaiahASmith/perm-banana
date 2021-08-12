from MetaCheck import MetaCheck
from Check import Check
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


def test_inside_from_checks():
    @banana
    class Test:
        test0 = Check(Permission(0b0001))
        test1 = Check(Permission(0b0010))
        test_both = test0 | test1
        test2 = Check(Permission(0b0101))
        test3 = Check(Permission(0b0110))
        test_and = test2 & test3

        def __init__(self, perms):
            self.permissions = Permission(perms)

    test = Test(0)
    assert not test.test0
    assert not test.test1
    assert not test.test_both
    assert not test.test_and
    test = Test(0b0001)
    assert test.test0
    assert not test.test1
    assert not test.test_both
    assert not test.test_and
    test = Test(0b0010)
    assert not test.test0
    assert test.test1
    assert not test.test_both
    assert not test.test_and
    test = Test(0b0011)
    assert test.test0
    assert test.test1
    assert test.test_both
    assert not test.test_and
    test = Test(0b0100)
    assert test.test_and


def test_inside_from_int():
    @banana
    class Test:
        test0: int = 0b0001
        test1: int = 0b0010
        test_both: int = test0 | test1

        def __init__(self, perms):
            self.permissions = Permission(perms)

    test = Test(0)
    assert not test.test0
    assert not test.test1
    assert not test.test_both
    test = Test(0b0001)
    assert test.test0
    assert not test.test1
    assert not test.test_both
    test = Test(0b0010)
    assert not test.test0
    assert test.test1
    assert not test.test_both
    test = Test(0b0011)
    assert test.test0
    assert test.test1
    assert test.test_both


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
