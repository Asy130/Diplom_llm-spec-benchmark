def check_preconditions(board):
    assert isinstance(board, list)
    assert len(board) == 3
    assert all(len(row) == 3 for row in board)

def check_postconditions(board, result):
    assert result in ("X", "O", None)