import string

import homework2.task5


def test_one_arg():
    assert homework2.task5.custom_range(string.ascii_lowercase, "g") == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]


def test_two_args():
    assert homework2.task5.custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_three_args():
    assert homework2.task5.custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]
