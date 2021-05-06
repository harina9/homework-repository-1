import pytest

from homework4.task3 import my_precious_logger


def test_error_case(capsys):
    text = "error: file not found"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.err == "error: file not found"


def test_without_error_case(capsys):
    text = "_error not found"
    my_precious_logger(text)
    captured = capsys.readouterr()
    assert captured.out == "_error not found"
