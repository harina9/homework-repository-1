from unittest.mock import Mock

import pytest
import requests

from homework4.task2 import count_dots_on_i


def test_positive_without_monkey_patch():
    assert count_dots_on_i("https://example.com/") == 59


def test_positive_with_monkey_patch(monkeypatch):
    request_mock = Mock()
    request_mock.return_value.text = "iiiaii"

    monkeypatch.setattr(requests, "get", request_mock)
    assert count_dots_on_i("something") == 5


def test_negative(monkeypatch):
    request_mock = Mock()
    request_mock.return_value.text = "no__letters"

    monkeypatch.setattr(requests, "get", request_mock)
    assert count_dots_on_i("path") == 0
