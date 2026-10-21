import pytest
import copy
from impl.T01.correct_a import winner as correct_func

def test_row_win():
    assert correct_func([["X", "X", "X"], ["O", "O", ""], ["", "", ""]]) == "X"

def test_col_win():
    assert correct_func([["O", "X", ""], ["O", "X", ""], ["O", "", ""]]) == "O"

def test_diag_win():
    assert correct_func([["X", "O", ""], ["O", "X", ""], ["", "", "X"]]) == "X"

def test_anti_diag_win():
    assert correct_func([["", "O", "X"], ["O", "X", ""], ["X", "", ""]]) == "X"

def test_no_winner():
    assert correct_func([["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]) is None

def test_input_not_modified():
    board = [["X", "O", ""], ["", "X", ""], ["", "", ""]]
    before = copy.deepcopy(board)
    correct_func(board)
    assert board == before