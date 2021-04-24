import pytest
from homework2.task4 import cache

counter = 0

def test_cache_decorator():
    @cache
    def cached_function():
        global counter
        counter += 1
        assert counter == 0
        cached_function()
        assert counter == 1
        cached_function()
        assert counter == 1