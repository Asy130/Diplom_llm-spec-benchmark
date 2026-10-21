def check_preconditions(row):
    assert isinstance(row, list)
    assert all(isinstance(x, int) and x >= 0 for x in row)

def check_postconditions(row, result):
    assert isinstance(result, list)
    assert len(result) == len(row)