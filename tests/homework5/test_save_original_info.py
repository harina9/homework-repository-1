import functools

from homework5.save_original_info import custom_sum, print_result


def test_save_original_info():
    if "name" == "__main__":
        assert (
            custom_sum.__doc__
            == "This function can sum any objects which have __add___"
        )
        assert custom_sum.__name__ == "custom_sum"
        assert (
            custom_sum.__original_func == "<function custom_sum at 0x0000019DFA4079D0>"
        )
