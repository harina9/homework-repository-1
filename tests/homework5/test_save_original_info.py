import functools

from homework5.save_original_info import add_attribute_for_function, custom_sum


def decorator(func):
    @functools.wraps(func)
    @add_attribute_for_function(func)
    def wrapper(*args, **kwargs):
        return func

    return wrapper


def some_func(*args, **kwargs):
    pass


decorated_func = decorator(some_func)


def test_save_original_info_saves_docs_of_custom_sum():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"


def test_save_original_info_saves_name_of_custom_sum():
    assert custom_sum.__name__ == "custom_sum"


def test_decorator_name_doc_original_info():
    assert decorated_func.__original_func == some_func
