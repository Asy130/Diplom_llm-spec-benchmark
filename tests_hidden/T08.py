import pytest
import copy
from impl.T08.correct_a import is_valid_row as correct_func

def test_valid_row():
    assert correct_func([1, 2, 3, 4, 5, 6, 7, 8, 9]) is True

def test_invalid_row():
    assert correct_func([1, 2, 3, 4, 5, 6, 7, 8, 1]) is False

def test_multiple_zeros():
    # R2: Zero is allowed multiple times
    assert correct_func([0, 0, 0, 1, 2, 3, 4, 5, 6]) is True

def test_empty_board():
    assert correct_func([0, 0, 0, 0, 0, 0, 0, 0, 0]) is True

def test_input_not_modified():
    # R4: Do not modify input
    row = [1, 2, 0, 0, 0, 0, 0, 0, 0]
    before = copy.deepcopy(row)
    correct_func(row)
    assert row == before