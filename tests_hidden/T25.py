import pytest
from impl.T25.correct_a import step as correct_func

def test_underpopulation():
    grid = [[True, False, False], [False, False, False], [False, False, False]]
    expected = [[False, False, False], [False, False, False], [False, False, False]]
    assert correct_func(grid) == expected

def test_blinker():
    # A blinker should oscillate
    grid = [
        [False, False, False],
        [True, True, True],
        [False, False, False]
    ]
    expected = [
        [False, True, False],
        [False, True, False],
        [False, True, False]
    ]
    assert correct_func(grid) == expected

def test_block_stays_same():
    # A 2x2 block is stable
    grid = [
        [True, True, False],
        [True, True, False],
        [False, False, False]
    ]
    assert correct_func(grid) == grid