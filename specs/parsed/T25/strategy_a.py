def check_preconditions(grid):
    assert isinstance(grid, list)
    assert len(grid) > 0

def check_postconditions(grid, result):
    assert isinstance(result, list)
    assert len(result) == len(grid)