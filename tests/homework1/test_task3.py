from homework1.task3 import find_maximum_and_minimum


def test_only_negative_numbers():
    assert find_maximum_and_minimum("tests/homework1/number1.txt") == (-56, -1)


def test_only_positive_numbers():
    assert find_maximum_and_minimum("tests/homework1/number2.txt") == (2, 789)


def test_positive_and_negative():
    assert find_maximum_and_minimum("tests/homework1/number3.txt") == (-19, 78)
