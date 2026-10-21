def step(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    new_grid = [[False for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            # Count live neighbors
            live_neighbors = 0
            for i in range(max(0, r-1), min(rows, r+2)):
                for j in range(max(0, c-1), min(cols, c+2)):
                    if (i, j) != (r, c) and grid[i][j]:
                        live_neighbors += 1
            
            # Apply rules
            if grid[r][c]:
                if live_neighbors == 2 or live_neighbors == 3:
                    new_grid[r][c] = True
            else:
                if live_neighbors == 3:
                    new_grid[r][c] = True
    return new_grid