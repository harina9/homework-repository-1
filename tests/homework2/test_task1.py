import homework2.task1


def test_first_function():
    assert homework2.task1.get_longest_diverse_words("data.txt") == [
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
    assert homework2.task1.get_rarest_char("data.txt") == "›"


def test_third_function():
    assert homework2.task1.count_punctuation_chars("data.txt") == 5305


def test_fourth_function():
    assert homework2.task1.count_non_ascii_chars("data.txt") == 2972


def test_fifth_function():
    assert homework2.task1.get_most_common_non_ascii_char("data.txt") == "ä"
