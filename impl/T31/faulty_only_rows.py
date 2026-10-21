def is_valid_reversi_move(board, x, y, color):
    if board[x][y] != "": return False
    opponent = "W" if color == "B" else "B"
    # BUG: Missing diagonal directions
    directions = [(-1,0), (1,0), (0,-1), (0,1)] 
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board[nx][ny] == opponent:
                found_opponent = True
            elif board[nx][ny] == color:
                if found_opponent: return True
                break
            else:
                break
            nx += dx
            ny += dy
    return False

# COUNTEREXAMPLE (Proves this is faulty):
# A board where a diagonal move captures pieces, but no horizontal/vertical moves are valid.
# Expected: True
# Actual: False