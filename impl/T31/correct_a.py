def is_valid_reversi_move(board, x, y, color):
    if board[x][y] != "": return False
    opponent = "W" if color == "B" else "B"
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
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