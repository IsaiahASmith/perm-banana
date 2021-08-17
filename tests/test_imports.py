"""
Tests if the imports are set up properly.
"""


def test_main():
    from perm_banana import banana, Check, MetaCheck, NameConflictException, Permission, PermissionHandler

    assert callable(banana)
    assert isinstance(Check, type)
    assert isinstance(MetaCheck, type)
    assert isinstance(NameConflictException, type)
    assert isinstance(Permission, type)
    assert isinstance(PermissionHandler, type)


def test_check_strategy():
    from perm_banana.CheckStrategy import (
        Strategy,
        StrategyCheck,
        StrategyHandler,
        StrategyPermission,
        StrategyPermissions,
    )

    assert isinstance(Strategy, type)
    assert isinstance(StrategyCheck, type)
    assert isinstance(StrategyHandler, type)
    assert isinstance(StrategyPermission, type)
    assert isinstance(StrategyPermissions, type)
