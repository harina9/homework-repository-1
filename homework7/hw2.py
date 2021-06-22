"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def deleting_backspace(file: str):
    new_str = []
    for letter in file:
        if letter != "#":
            new_str.append(letter)
        else:
            try:
                new_str.pop()
            except IndexError:
                pass

    return "".join(new_str)


def backspace_compare(first: str, second: str):
    if deleting_backspace(first) == deleting_backspace(second):
        return True
    return False


print(backspace_compare("ab#u", "as#d"))
