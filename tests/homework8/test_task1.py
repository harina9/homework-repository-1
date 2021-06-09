from unittest import mock

import pytest

from homework8.task1 import KeyValueStorage

storage = KeyValueStorage("task1.txt")


def test_key():
    assert storage["name"] == "kek"


def test_attr():
    assert storage.song == "shadilay"


def test_integer_value():
    assert isinstance(storage.power, int)


def test_key_error():
    mock_open = mock.mock_open(read_data="1=smth")
    with pytest.raises(ValueError):
        with mock.patch("builtins.open", mock_open):
            KeyValueStorage(mock_open)
