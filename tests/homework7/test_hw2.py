import pytest

from homework7.hw2 import backspace_compare


def test_same_strings_with_1_backspace():
    assert backspace_compare("ab#c", "ad#c")


def test_same_strings_with_many_backspaces():
    assert backspace_compare("a##c", "#a#c")


def test_empty_strings_with_backspace_only():
    assert backspace_compare("#", "##")


def test_negative():
    assert not backspace_compare("a#c", "b")
