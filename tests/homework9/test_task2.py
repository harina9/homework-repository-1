from homework9.task2 import SupressorAsClass, supressor


def test_class_with_error():
    with SupressorAsClass(IndexError):
        [][1]


def test_class_without_error():
    with SupressorAsClass(IndexError):
        [1][2]


def test_function_with_error():
    with supressor(IndexError):
        [][1]


def test_function_without_error():
    with supressor(IndexError):
        [][1]
