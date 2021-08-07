from Permission import Permission
from Perm import Perm
from Check import Check
from banana import banana


def test_init():
    @banana({})
    class Test:
        def __init__(self, test):
            self.test = test

    test = Test(0)
    assert test.test == 0


def test_with_check():
    @banana({Perm("test", Check(lambda *_: True))})
    class Test:
        def __init__(self, test):
            self.test2 = test

    test = Test(0)
    assert test.test2 == 0
    assert test.test
