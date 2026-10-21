import pytest
from impl.T14.correct_a import merge_row as correct_func

def test_basic_merge():
    assert correct_func([2, 2, 0, 0]) == [4, 0, 0, 0]

def test_double_merge():
    assert correct_func([2, 2, 2, 2]) == [4, 4, 0, 0]

def test_merge_last_two():
    assert correct_func([2, 2, 4]) == [4, 4, 0]

def test_no_merge():
    assert correct_func([2, 4, 8, 16]) == [2, 4, 8, 16]

def test_zeros_shifted():
    assert correct_func([0, 2, 0, 2]) == [4, 0, 0, 0]

def test_length_preserved():
    assert len(correct_func([2, 2, 2, 0])) == 4