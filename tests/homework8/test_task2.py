import pytest

from homework8.task2 import TableData

presidents = TableData(database_name="example.sqlite", table_name="presidents")


def test_len_method():
    assert len(presidents) == 3


def test_getitem():
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")


def test_contains():
    assert "Trump" in presidents


def test_keys():
    ages = [president["age"] for president in presidents]
    assert ages == [999, 1337, 101]
