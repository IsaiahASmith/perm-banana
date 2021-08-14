from perm_banana.Permission import Permission


def test_initialization():
    Permission(0)


def test_int():
    assert int(Permission(0)) == 0
    assert int(Permission(1)) == 1


def test_bool():
    assert not bool(Permission(0))
    assert bool(Permission(1))


def test_invert():
    perm = Permission(0b1100)
    assert ~0b1100 == int(~perm)


def test_and():
    perm0 = Permission(0b1110)
    perm1 = Permission(0b0111)
    assert (perm0 & perm1) == Permission(0b0110)


def test_iand():
    perm0 = Permission(0b1110)
    perm1 = Permission(0b0111)
    perm0 &= perm1
    assert perm0 == Permission(0b0110)


def test_or():
    perm0 = Permission(0b1000)
    perm1 = Permission(0b0001)
    assert (perm0 | perm1) == Permission(0b1001)


def test_ior():
    perm0 = Permission(0b1000)
    perm1 = Permission(0b0001)
    perm0 |= perm1
    assert perm0 == Permission(0b1001)


def test_add():
    perm0 = Permission(0b1000)
    perm1 = Permission(0b0001)
    assert (perm0 + perm1) == Permission(0b1001)


def test_iadd():
    perm0 = Permission(0b1000)
    perm1 = Permission(0b0001)
    perm0 += perm1
    assert perm0 == Permission(0b1001)


def test_sub():
    perm0 = Permission(0b1110)
    perm1 = Permission(0b1101)
    assert (perm0 - perm1) == Permission(0b0010)


def test_isub():
    perm0 = Permission(0b1110)
    perm1 = Permission(0b1101)
    perm0 -= perm1
    assert perm0 == Permission(0b0010)


def test_lt():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert perm1 < perm0
    assert not perm0 < perm1
    assert not perm0 < perm0


def test_le():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert perm1 <= perm0
    assert not perm0 <= perm1
    assert perm0 <= perm0


def test_eq():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert not perm1 == perm0
    assert not perm0 == perm1
    assert perm0 == perm0
    assert perm1 == perm1


def test_ne():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert perm1 != perm0
    assert perm0 != perm1
    assert not perm0 != perm0
    assert not perm1 != perm1


def test_gt():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert perm0 > perm1
    assert not perm1 > perm0
    assert not perm0 > perm0


def test_ge():
    perm0 = Permission(0b0001)
    perm1 = Permission(0b0000)
    assert perm0 >= perm1
    assert not perm1 >= perm0
    assert perm0 >= perm0
