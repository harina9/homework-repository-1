"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions

fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return the list of strings from 1 to n where each number that is multiple to 3 is represented
    as "Fizz", each number which is multiple to 5 is represented as "Buzz" and both to 3 and 5 - "Fizz Buzz"
    :param n: int
    :return: List[str]

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']

    >>> fizzbuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']

    >>> fizzbuzz(1)
    ['1']
    """
    line_of_numbers = []
    for element in range(1, n + 1):
        if element % 3 == 0 and element % 5 == 0:
            line_of_numbers.append("Fizz Buzz")
        elif element % 3 == 0:
            line_of_numbers.append("Fizz")
        elif element % 5 == 0:
            line_of_numbers.append("Buzz")
        else:
            line_of_numbers.append(str(element))

    return line_of_numbers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
