import pytest

from homework2.task2 import major_and_minor_elem


def test_positive_result():
    """Testing that the code shows the correct result"""
    assert major_and_minor_elem([2, 3, 3, 3, 4, 4]) == (3, 2)


def test_one_common_element():
    """Testing list with one common element"""
    assert major_and_minor_elem([5, 5, 5, 5]) == (5, 5)
