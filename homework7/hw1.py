"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    occurrences = 0
    if isinstance(tree, dict):
        tree = tree.values()
    for value in tree:
        if value == element:
            occurrences += 1
        if isinstance(value, (str, bool, int, set, tuple)):
            continue
        else:
            occurrences += find_occurrences(value, element)
    return occurrences
