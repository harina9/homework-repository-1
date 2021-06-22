"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return f"{board[1][1]} wins"
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return f"{board[1][1]} wins"
    for string, array in enumerate(board):
        if array[0] == array[1] == array[2] != "-":
            return f"{array[1]} wins"
        elif board[0][string] == board[1][string] == board[2][string] != "-":
            return f"{board[0][string]} wins"
    for massive in board:
        if "-" in massive:
            return f"unfinished"
        else:
            return f"draw"
