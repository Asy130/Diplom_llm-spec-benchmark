def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    return None

# COUNTEREXAMPLE (Proves this is faulty):
# board = [["X", "O", ""], ["O", "X", ""], ["", "", "X"]]
# Expected: "X" (diagonal win)
# Actual: None