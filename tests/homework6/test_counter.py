import pytest

from homework6.counter import User, instances_counter


@instances_counter
class User:
    pass


def test_first_call():
    assert User.get_created_instances() == 0


def test_with_instances():
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances():
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
