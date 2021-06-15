from functools import partial
from typing import Dict, List, Union


class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """

    def keyword_filter_func(keywords, key, value):
        return keywords.get(key) == value

    new_funcs = []
    for key, value in keywords.items():
        filter_funcs = partial(keyword_filter_func, key=key, value=value)
        new_funcs.append(filter_funcs)
    return Filter(new_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

print(make_filter(name="Bill", type="person").apply(sample_data))
