import pytest

from homework11.task1 import SimplifiedEnum


def test_metaclass_simplified_sets_colors_enum_attrs_in__keys():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.ORANGE == "ORANGE"
