import pytest

from homework6.counter import User


def test_first_user():
    assert User.get_created_instances() == 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3


class User2(User):
    def __init__(self, a):
        self.a = a
        super().__init__()


def test_another_user():
    assert User2.get_created_instances() == 0
    User2("test2"), User2("test2")
    assert User2.get_created_instances() == 2
