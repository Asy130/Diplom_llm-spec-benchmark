def step(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[False for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            live_neighbors = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue
                    # BUG: Uses modulo operator to wrap edges instead of treating them as dead
                    if grid[(r + i) % rows][(c + j) % cols]: 
                        live_neighbors += 1
            
            if grid[r][c] and live_neighbors in (2, 3):
                new_grid[r][c] = True
            elif not grid[r][c] and live_neighbors == 3:
                new_grid[r][c] = True
    return new_grid

# COUNTEREXAMPLE (Proves this is faulty):
# Input: A single live cell in the top-left corner of a 3x3 grid.
# [[True, False, False], [False, False, False], [False, False, False]]
# Expected: [[False, False, False], ...] (dies of underpopulation, 0 neighbors)
# Actual: [[True, False, False], ...] (wraps around and thinks it has neighbors)