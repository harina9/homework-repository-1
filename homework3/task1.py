from typing import Callable
from unittest.mock import Mock, call

import pytest


def cache(times):
    def cached(func) -> Callable:
        stored_values = []

        def wrapper(*args, **kwargs):
            key_of_call = args, kwargs
            for key, value in stored_values:
                if key == key_of_call:
                    return value
            result = func(*args, **kwargs)
            stored_values.append((key_of_call, result))
            return result

        return wrapper

    return cached


@cache(times=1)
def f(a, b):
    return a + b


def test_cache():
    mock = Mock()
    cached_function = cache(times=1)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3)]
