from typing import Callable
from unittest.mock import Mock, call

import pytest


def make_key(args, kwargs):
    return args, tuple(sorted(kwargs.items()))


def cache(times):
    def wrapper(fun):
        cache_data = {}

        def inner(*args, **kwargs):
            key = make_key(args, kwargs)
            if key not in cache_data:
                result = fun(*args, **kwargs)
                cache_data[key] = [result, 0]
            result, called = cache_data[key]
            if called > times:
                return fun(*args, **kwargs)
            else:
                cache_data[key][1] += 1

        return inner

    return wrapper
