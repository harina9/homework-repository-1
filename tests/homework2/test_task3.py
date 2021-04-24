import pytest
from homework2.task3 import combinations


def test_two_elements():
    """Testing that the combination works with 2-elements lists"""
    assert combinations([1, 2], [3, 5]) == [(1, 3), (1, 5), (2, 3), (2, 5)]


