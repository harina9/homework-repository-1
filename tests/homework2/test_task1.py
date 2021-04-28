import pytest

from homework2.task1 import (
    count_non_ascii_chars,
    count_punctuation_chars,
    get_longest_diverse_words,
    get_most_common_non_ascii_char,
    get_rarest_char,
)


def test_first_function():
    assert get_longest_diverse_words("data.txt") == [
        "Nichtkämpfern",
        "Entscheidungsschlacht",
        "Schöpfungsmacht",
        "Werkstättenlandschaft",
        "Schicksalsfiguren",
        "politisch-strategischen",
        "Selbstverständlich",
        "résistance-Bewegungen",
        "unmißverständliche",
        "Bevölkerungsabschub",
    ]


def test_second_function():
    assert get_rarest_char("data.txt") == "›"


def test_third_function():
    assert count_punctuation_chars("data.txt") == 5305


def test_fourth_function():
    assert count_non_ascii_chars("data.txt") == 2972


def test_fifth_function():
    assert get_most_common_non_ascii_char("data.txt") == "ä"
