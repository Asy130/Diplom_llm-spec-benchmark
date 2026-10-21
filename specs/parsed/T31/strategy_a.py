def check_preconditions(board, x, y, color):
    assert isinstance(board, list)
    assert color in ("B", "W")

def check_postconditions(result):
    assert isinstance(result, bool)