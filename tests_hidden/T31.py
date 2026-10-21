import pytest
from impl.T31.correct_a import is_valid_reversi_move as correct_func

def create_empty_board():
    return [["" for _ in range(8)] for _ in range(8)]

def test_invalid_empty_board():
    board = create_empty_board()
    assert correct_func(board, 3, 3, "B") is False

def test_occupied_cell():
    board = create_empty_board()
    board[3][3] = "B"
    assert correct_func(board, 3, 3, "B") is False

def test_valid_horizontal():
    board = create_empty_board()
    board[3][3] = "W"
    board[3][4] = "B"
    # 'B' can place at (3, 2) to trap 'W' at (3, 3)
    assert correct_func(board, 3, 2, "B") is True

def test_valid_diagonal():
    board = create_empty_board()
    board[3][3] = "W"
    board[4][4] = "B"
    # 'B' can place at (2, 2) to trap 'W'
    assert correct_func(board, 2, 2, "B") is True