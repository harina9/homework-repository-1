import homework2.task1

path_data = "./tests/homework2/data.txt"


def test_first_function():
    assert homework2.task1.get_longest_diverse_words(path_data) == [
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
    assert homework2.task1.get_rarest_char(path_data) == "›"


def test_third_function():
    assert homework2.task1.count_punctuation_chars(path_data) == 5305


def test_fourth_function():
    assert homework2.task1.count_non_ascii_chars(path_data) == 2972


def test_fifth_function():
    assert homework2.task1.get_most_common_non_ascii_char(path_data) == "ä"
