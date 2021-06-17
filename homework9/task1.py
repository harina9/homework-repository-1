"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: [str, str]) -> Iterator:
    file1 = Path(file_list[0])
    file2 = Path(file_list[1])
    file1 = file1.read_text().splitlines()
    file2 = file2.read_text().splitlines()
    list_merged = []
    len1 = len(file1)
    len2 = len(file2)
    for index in range(max(len1, len2)):
        if index + 1 <= len1:
            list_merged += [int(file1[index])]
        if index + 1 <= len2:
            list_merged += [int(file2[index])]
    return list_merged


print(merge_sorted_files(["file1.txt", "file2.txt"]))
