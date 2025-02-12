"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""

import string
from collections import OrderedDict
from typing import List

from nltk import word_tokenize


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        text_tokens = word_tokenize(text)
        d = {}

        for word in text_tokens:
            result = "".join(OrderedDict.fromkeys(word))
            d[result] = word

        longest_cases = sorted(d.keys(), key=len)[-11:-1]

        final = []
        for element in longest_cases:
            final.append(d[element])

        return final


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        punctuation_chars = string.punctuation
        count = 0

        for element in text:
            if element in punctuation_chars:
                count += 1
        return count


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        every_char = {}

        for element in text:
            if element in every_char:
                every_char[element] += 1
            else:
                every_char[element] = 1

        rarest_char = min(every_char, key=every_char.get)
        return rarest_char


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        count_char = 0

        for line in text:
            for char in line:
                if not char.isascii():
                    count_char += 1

        return count_char


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as file:
        text = file.read()
        d = {}

        for line in text:
            for char in line:
                if not char.isascii():
                    if char in d:
                        d[char] += 1
                    else:
                        d[char] = 1

        common_char = max(d, key=d.get)
        return common_char
