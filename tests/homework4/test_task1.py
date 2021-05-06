import pytest

from homework4.task1 import read_magic_number


def test_positive_case(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    new_file = path / "hello.txt"
    new_file.write_text("1")
    assert read_magic_number(new_file)


def test_negative_case(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    new_file = path / "hello.txt"
    new_file.write_text("3")
    assert not read_magic_number(new_file)


def test_string_case(tmp_path):
    path = tmp_path / "sub"
    path.mkdir()
    new_file = path / "hello.txt"
    new_file.write_text("abc")
    with pytest.raises(ValueError):
        assert read_magic_number(new_file)
