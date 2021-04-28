"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def generate_fibonacci(start_el):
    first, second = 0, 1
    while True:
        if first >= start_el:
            yield first
        first, second = second, first + second


def check_fibonacci(data: Sequence[int]) -> bool:
    for our_number, fib_number in zip(data, generate_fibonacci(5)):
        if our_number != fib_number:
            return False

    return True
