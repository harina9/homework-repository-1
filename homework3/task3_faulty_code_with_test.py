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
    filter_funcs = []
    for key, value in keywords.items():

        def keyword_filter_func(value):
            return value[key] == value

        filter_funcs.append(keyword_filter_func)
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]

print(make_filter(name="polly", type="bird").apply(sample_data))


def test_faulty_case_number_1():
    """Testing that make_filter function does not return True because of the line
    value[key] == value"""
    functions = make_filter(name="polly", type="bird").functions
    item = {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    assert not any(i(item) for i in functions)
