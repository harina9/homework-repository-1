from homework9.task3 import universal_file_counter


def test_universal_file_counter_without_tokenizer():
    assert universal_file_counter("file_for_3.txt") == 6


def test_universal_file_counter_with_tokenizer():
    assert universal_file_counter("file_for_3.txt", str.split) == 6
