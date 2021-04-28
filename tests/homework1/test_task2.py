from homework1.task2 import check_fibonacci


def test_fibonacci_sequence():
    assert check_fibonacci([5, 8, 13])


def test_not_fibonacci_sequence():
    assert not check_fibonacci([4, 6, 10])
