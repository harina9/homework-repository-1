import pytest

from homework7.hw3 import tic_tac_toe_checker


def test_x_wins():
    x_wins = [["-", "x", "o"], ["-", "x", "o"], ["x", "x", "x"]]
    assert tic_tac_toe_checker(x_wins) == "x wins"


def test_y_wins():
    y_wins = [["y", "x", "o"], ["x", "y", "y"], ["x", "x", "y"]]
    assert tic_tac_toe_checker(y_wins) == "y wins"


def test_draw():
    draw = [["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]]
    assert tic_tac_toe_checker(draw) == "draw"


def test_unfinished():
    unfinished = [["-", "-", "o"], ["-", "-", "o"], ["x", "o", "-"]]
    assert tic_tac_toe_checker(unfinished) == "unfinished"
