import pytest

from homework3.task4 import is_armstrong


def test_positive_case():
    assert is_armstrong(407) == "Is Armstrong number"


def test_negative_case():
    assert is_armstrong(10) == "Is not Armstrong number"


def test_zero_case():
    assert is_armstrong(0) == "Is Armstrong number"


def test_one_case():
    assert is_armstrong(1) == "Is Armstrong number"
