# Benchmark Tasks

Description of 40 game-themed Python tasks used to evaluate LLM-generated
specifications. For each task, the signature, natural-language description,
requirements, logic, boundary cases, and invariants are provided.

---

## Summary Table

| ID  | Domain           | Task Name                |
|-----|------------------|--------------------------|
| T01 | Tic-tac-toe      | Winner detection         |
| T02 | Tic-tac-toe      | Move validity            |
| T03 | Chess            | Rook move                |
| T04 | Chess            | Bishop move              |
| T05 | Chess            | King under attack        |
| T06 | Chess            | Knight moves             |
| T07 | Checkers         | Mandatory capture        |
| T08 | Sudoku           | Row validity             |
| T09 | Sudoku           | Board validity           |
| T10 | Minesweeper      | Adjacent mines count     |
| T11 | Minesweeper      | Cell reveal              |
| T12 | Fifteen puzzle   | Move validity            |
| T13 | Fifteen puzzle   | Solvability              |
| T14 | 2048             | Row merge                |
| T15 | 2048             | Move left                |
| T16 | 2048             | Move right               |
| T17 | 2048             | Game over                |
| T18 | Snake            | Step                     |
| T19 | Snake            | Collision                |
| T20 | Snake            | Grow on eat              |
| T21 | Tetris           | Piece rotation           |
| T22 | Tetris           | Line clearing            |
| T23 | Tetris           | Position validity        |
| T24 | Tetris           | Piece drop               |
| T25 | Conway           | Step                     |
| T26 | Conway           | Neighbors                |
| T27 | Map              | Pathfinding              |
| T28 | Battleship       | Ship hit                 |
| T29 | Battleship       | Ship sunk                |
| T30 | Battleship       | All ships sunk           |
| T31 | Reversi          | Move validity            |
| T32 | Reversi          | Apply move               |
| T33 | Dice             | Roll                     |
| T34 | Dice             | Roll sum                 |
| T35 | Fifteen puzzle   | Next move                |
| T36 | Tic-tac-toe      | Best move                |
| T37 | HP / damage      | Apply damage             |
| T38 | Experience       | Level up                 |
| T39 | Inventory        | Add item                 |
| T40 | Inventory        | Total weight             |

---

## Group A. Board Games

### T01. Winner detection (tic-tac-toe)

**Signature:** `def winner(board: list[list[str]]) -> str | None`

**Description.** The function receives a 3×3 game board. Each cell may contain:

- `'X'`;
- `'O'`;
- an empty string `''`.

The function checks whether anyone has won. A player wins if three of their
symbols are placed:

- in the same row;
- in the same column;
- on one of the diagonals.

If a winner is found, the function returns their symbol: `'X'` or `'O'`. If
there is no winner or the game is still in progress, the function returns
`None`.

**Requirements:**
- **R1.** Return `'X'` if three `'X'` form a line.
- **R2.** Return `'O'` if three `'O'` form a line.
- **R3.** Return `None` if there is no winner.
- **R4.** Do not modify the input board.

**Logic.** Eight lines are checked: 3 rows, 3 columns, 2 diagonals. If a line
contains three identical non-empty symbols, that is the winner.

**Boundary cases:**
- Empty board → `None`.
- Draw → `None`.
- Two lines at once → the first one found.

**Invariants:**
- Result ∈ {`'X'`, `'O'`, `None`}.
- Swapping `X` ↔ `O` symmetrically changes the result.
- Input is not modified.

---

### T02. Move validity (tic-tac-toe)

**Signature:** `def is_valid_move(board, x: int, y: int) -> bool`

**Description.** The function receives a 3×3 game board and cell coordinates.

It returns `True` if:

- the coordinates are within the board — from 0 to 2;
- the chosen cell is empty.

In all other cases, the function returns `False`.

The original game board is not modified.

**Requirements:**
- **R1.** `True` if coordinates are within `[0, 2]`.
- **R2.** `True` only if the cell is empty (`''`).
- **R3.** `False` if coordinates are out of bounds.
- **R4.** Do not modify the input board.

**Logic.** Check bounds `0 ≤ x ≤ 2`, `0 ≤ y ≤ 2`. Check
`board[x][y] == ''`.

**Boundary cases:**
- Negative coordinates → `False`.
- Coordinates ≥ 3 → `False`.
- Occupied cell → `False`.

**Invariants:**
- Idempotence.
- Input is not modified.

---

### T03. Rook move (chess)

**Signature:** `def is_rook_move(board, start: tuple, end: tuple) -> bool`

**Description.** The function receives an 8×8 chess board, a start square, and
an end square. It checks whether the rook can make such a move.

The function returns `True` if:

- the rook moves horizontally or vertically;
- there are no other pieces between the start and end squares;
- the end square is empty or occupied by an opponent's piece.

In all other cases, the function returns `False`.

**Requirements:**
- **R1.** `True` only if the move is along a row or column.
- **R2.** `True` only if the path is clear.
- **R3.** `False` if the end square is occupied by a friendly piece.
- **R4.** Do not modify the board.

**Logic.** `start.row == end.row` or `start.col == end.col`. There are no pieces
between `start` and `end`. `end` is empty or holds an opponent's piece.

**Boundary cases:**
- `start == end` → `False`.
- Diagonal move → `False`.
- Obstacle on the path → `False`.

**Invariants:**
- Symmetry: `is_rook_move(s, e) == is_rook_move(e, s)` without capture.
- Input is not modified.

---

### T04. Bishop move (chess)

**Signature:** `def is_bishop_move(board, start: tuple, end: tuple) -> bool`

**Description.** The function receives an 8×8 chess board and start and end
square coordinates.

It returns `True` if:

- the bishop moves diagonally;
- the row and column distances are equal;
- there are no other pieces between the start and end squares;
- the end square is empty or occupied by an opponent's piece.

In all other cases, the function returns `False`.

**Requirements:**
- **R1.** `True` only if `|Δrow| == |Δcol|`.
- **R2.** `True` only if the path is clear.
- **R3.** `False` if the end square is occupied by a friendly piece.
- **R4.** Do not modify the board.

**Logic.** `|start.row - end.row| == |start.col - end.col|`. There are no pieces
between `start` and `end`.

**Boundary cases:**
- Straight move → `False`.
- Obstacle on the diagonal → `False`.

**Invariants:**
- Symmetry.
- Input is not modified.

---

### T05. King under attack (chess)

**Signature:** `def is_king_attacked(board, color: str) -> bool`

**Description.** The function receives an 8×8 chess board and the king's color:
`'white'` or `'black'`.

It checks whether the king of this color is under attack by an opponent's piece.

Attacks from all pieces are considered:

- pawns;
- knights;
- bishops;
- rooks;
- queens;
- the opponent's king.

The function returns `True` if the king is attacked by at least one piece. If
there is no attack, it returns `False`.

The chess board is not modified.

**Requirements:**
- **R1.** `True` if at least one opponent piece attacks the king.
- **R2.** Correctly account for pawn direction.
- **R3.** Consider all piece types.
- **R4.** Do not modify the board.

**Logic.** Find the king. For each opponent piece, check whether it attacks the
king.

**Boundary cases:**
- No king → `False` or error.
- King in a corner.

**Invariants:**
- If all opponent pieces are removed → `False`.

---

### T06. Knight moves (chess)

**Signature:** `def knight_moves(board, pos: tuple) -> list[tuple]`

**Description.** The function receives an 8×8 chess board and the knight's
position.

It returns a list of all squares the knight can move to. The knight can move to
a square if:

- it is within the board;
- it is not occupied by a piece of the same color.

The order of squares in the list does not matter. If the knight cannot make any
move, the function returns an empty list `[]`.

**Requirements:**
- **R1.** Return a list of valid squares.
- **R2.** All squares are within the board.
- **R3.** Exclude squares occupied by friendly pieces.
- **R4.** Do not modify the board.

**Logic.** 8 positions `(|Δrow|, |Δcol|) ∈ {(1,2), (2,1)}`. Filter: within
bounds, not a friendly piece.

**Boundary cases:**
- Knight in a corner → 2 moves.
- All squares occupied by friendly pieces → `[]`.

**Invariants:**
- All coordinates are within `[0, 7]`.

---

### T07. Mandatory capture (checkers)

**Signature:** `def must_capture(board, color: str) -> bool`

**Description.** The function receives an 8×8 checkers board and the player's
color.

It checks whether at least one checker of this player can make a mandatory
capture. To do so, the checker must:

- jump over an opponent's checker;
- land on a free square immediately behind it.

The function returns `True` if such a move is possible for at least one checker.
If no checker can make a capture, the function returns `False`.

**Requirements:**
- **R1.** `True` if at least one valid capture exists.
- **R2.** Consider only pieces of the specified color.
- **R3.** `False` if no capture is possible.
- **R4.** Do not modify the board.

**Logic.** For each player's piece, check 4 diagonals: the neighboring square
holds an opponent's piece, and the square behind it is empty.

**Boundary cases:**
- No opponent pieces → `False`.
- All diagonals blocked → `False`.

**Invariants:**
- Input is not modified.

---

### T08. Row validity (sudoku)

**Signature:** `def is_valid_row(row: list[int]) -> bool`

**Description.** The function receives a list of 9 numbers — one sudoku row.

It checks whether this row is valid. A row is valid if the numbers from 1 to 9
do not repeat.

Zero means an empty cell — there can be any number of such cells.

The function returns `True` if the row is valid. If any number from 1 to 9
appears more than once, the function returns `False`.

**Requirements:**
- **R1.** `True` if there are no repeated numbers 1–9.
- **R2.** Zero is allowed multiple times.
- **R3.** `False` if any number 1–9 repeats.
- **R4.** Do not modify the input list.

**Logic.** Take non-zero values. Check uniqueness.

**Boundary cases:**
- All zeros → `True`.
- Duplicate 5 → `False`.

**Invariants:**
- Permutation does not change the result.

---

### T09. Board validity (sudoku)

**Signature:** `def is_valid_board(board: list[list[int]]) -> bool`

**Description.** The function receives a 9×9 sudoku board.

It checks whether the whole board is valid. A board is valid if the numbers
from 1 to 9 do not repeat:

- in each row;
- in each column;
- in each 3×3 block.

Zero means an empty cell and is allowed in any quantity.

The function returns `True` if the board is fully valid. If there is at least
one violation, the function returns `False`.

**Requirements:**
- **R1.** All rows are valid.
- **R2.** All columns are valid.
- **R3.** All 3×3 blocks are valid.
- **R4.** Do not modify the input board.

**Logic.** Check 9 rows, 9 columns, 9 3×3 blocks.

**Boundary cases:**
- Empty board → `True`.
- One duplicate → `False`.

**Invariants:**
- Transposition preserves validity.

---

### T10. Adjacent mines count (minesweeper)

**Signature:** `def count_adjacent(mines, x: int, y: int) -> int`

**Description.** The function receives a minesweeper board and cell coordinates.

The minesweeper board is a matrix where `True` means a mine and `False` means an
empty cell.

The function counts how many mines are in the eight neighboring cells —
horizontally, vertically, and diagonally.

The specified cell itself is not counted. Cells outside the board are ignored.

The function returns the number of mines — an integer from 0 to 8.

**Requirements:**
- **R1.** Return the number of mines among the 8 neighbors.
- **R2.** Do not count the cell itself.
- **R3.** Ignore cells outside the board.
- **R4.** Do not modify the input board.

**Logic.** For each of the 8 positions around `(x, y)`: if within bounds and a
mine → `count++`.

**Boundary cases:**
- Corner → 3 neighbors.
- Center → 8 neighbors.

**Invariants:**
- `0 ≤ result ≤ 8`.
- Reflection symmetry.

---

### T11. Cell reveal (minesweeper)

**Signature:** `def reveal(board, x: int, y: int) -> board`

**Description.** The function receives a minesweeper board and cell coordinates.

It reveals the specified cell according to the rules of the game:

- if the cell contains a mine — the game ends;
- if the cell is empty and there are no mines nearby — all neighboring empty
  cells are revealed recursively;
- if the cell is already revealed — the board is not modified.

The function returns a new board with revealed cells.

**Requirements:**
- **R1.** Reveal the specified cell.
- **R2.** With zero adjacent mines — recursively reveal neighbors.
- **R3.** A mine ends the game.
- **R4.** Do not modify already revealed cells.

**Logic.** If a mine → Game Over. If `count_adjacent == 0` → recurse into
neighbors.

**Boundary cases:**
- Revealing a mine → Game Over.
- Recursion stops at the board edge.
- Cycles: do not process revealed cells twice.

**Invariants:**
- The set of revealed cells only grows.
- Input is not modified.

---

### T12. Move validity (fifteen puzzle)

**Signature:** `def can_move(board, tile: int) -> bool`

**Description.** The function receives a 4×4 fifteen puzzle board and a tile
number.

The board contains numbers from 1 to 15 and zero for the empty cell.

The function checks whether the specified tile can be moved. A tile can be moved
if it is an immediate neighbor of the empty cell — that is, in the same row or
column and adjacent.

The function returns `True` if the tile can be moved. In all other cases —
`False`.

**Requirements:**
- **R1.** `True` if the tile is adjacent to the empty cell.
- **R2.** `False` if the tile is not adjacent.
- **R3.** `False` for the empty cell (0).
- **R4.** Do not modify the input board.

**Logic.** Find the positions of `tile` and `0`. Check adjacency:
`|Δrow| + |Δcol| == 1`.

**Boundary cases:**
- Tile in a corner, empty cell next to it → `True`.
- One cell apart → `False`.

**Invariants:**
- Input is not modified.

---

### T13. Solvability (fifteen puzzle)

**Signature:** `def is_solvable(board) -> bool`

**Description.** The function receives a 4×4 fifteen puzzle board.

It checks whether the puzzle can be solved, that is, whether the numbers can be
arranged in order.

To do so, the function:

- counts the number of inversions — pairs of numbers where a larger number
  comes before a smaller one, excluding zero;
- determines the position of the empty cell.

If the board width is odd, solvability depends only on the parity of
inversions. If it is even, the row of the empty cell is also taken into
account.

The function returns `True` if the puzzle is solvable, and `False` otherwise.

**Requirements:**
- **R1.** Count inversions excluding 0.
- **R2.** Account for the empty cell position.
- **R3.** Return `True` if the configuration is solvable.
- **R4.** Do not modify the input board.

**Logic.** Inversions: pairs `(i, j)`, `i < j`, `board[i] > board[j]`,
`board[i] ≠ 0`. For even width: `(inversions + row of empty from bottom) is odd`
→ solvable.

**Boundary cases:**
- Solved board → `True`.
- One swap → depends on parity.

**Invariants:**
- Input is not modified.

---

## Group B. Arcade Games

### T14. Row merge (2048)

**Signature:** `def merge_row(row: list[int]) -> list[int]`

**Description.** The function receives a list of integers — one row of the 2048
game board.

It performs a left shift and merges equal numbers according to the rules of the
game:

- two equal tiles merge into one with doubled value and take the leftmost
  position;
- each tile merges at most once per move;
- zeros shift to the right.

The function returns a new list. The list length is unchanged. The order of
non-zero numbers is preserved.

**Requirements:**
- **R1.** Two equal tiles merge into one with doubled value.
- **R2.** Each tile merges at most once.
- **R3.** The order of non-zero numbers is preserved.
- **R4.** The list length is unchanged.

**Logic.** Remove zeros. Iterate: if two neighbors are equal → merge, skip the
next. Pad with zeros to the original length.

**Boundary cases:**
- `[2,2,2,2]` → `[4,4,0,0]`.
- `[2,2,4]` → `[4,4,0]`.
- `[0,0,0,0]` → `[0,0,0,0]`.

**Invariants:**
- Sum is preserved.
- Length is preserved.
- Order of non-zero numbers is preserved.

---

### T15. Move left (2048)

**Signature:** `def move_left(board) -> board`

**Description.** The function receives a 4×4 2048 board.

It applies a left shift and merge to all rows simultaneously.

The function returns a new board. No new tiles are added. The sum of all
elements is preserved.

**Requirements:**
- **R1.** Apply `merge_row` to all rows.
- **R2.** The sum of elements is preserved.
- **R3.** The number of non-zero cells does not increase.
- **R4.** Do not modify the input board.

**Logic.** Call `merge_row` for each row.

**Boundary cases:**
- Empty board → no changes.

**Invariants:**
- Sum is preserved.
- Input is not modified.

---

### T16. Move right (2048)

**Signature:** `def move_right(board) -> board`

**Description.** The function receives a 4×4 2048 board.

It applies a right shift and merge to all rows simultaneously.

The function returns a new board. No new tiles are added.

**Requirements:**
- **R1.** Right shift and merge.
- **R2.** The sum of elements is preserved.
- **R3.** The number of non-zero cells does not increase.
- **R4.** Do not modify the input board.

**Logic.** Reverse the row, `merge_row`, reverse back.

**Boundary cases:**
- Symmetric to T15.

**Invariants:**
- Same as T15.

---

### T17. Game over (2048)

**Signature:** `def is_game_over(board) -> bool`

**Description.** The function receives a 4×4 2048 board.

It checks whether the game is over. The game is over if:

- there are no empty cells;
- there is no way to merge two adjacent equal tiles horizontally or vertically.

The function returns `True` if the game is over. In all other cases — `False`.

**Requirements:**
- **R1.** `False` if there is an empty cell.
- **R2.** `False` if a merge is possible.
- **R3.** `True` if no moves are possible.
- **R4.** Do not modify the input board.

**Logic.** There is a `0` → `False`. There is a pair of equal neighbors →
`False`. Otherwise `True`.

**Boundary cases:**
- Full board with no pairs → `True`.
- Full board with a pair → `False`.

**Invariants:**
- Input is not modified.

---

### T18. Snake step (snake)

**Signature:** `def step(state, direction: str) -> state`

**Description.** The function receives the state of the game "Snake" and a
movement direction.

The state contains:

- coordinates of the snake segments, where the head is the first element;
- coordinates of the food;
- the board size.

The function returns a new state after one step:

- the head moves one cell in the given direction;
- if the head lands on the food — the snake grows by one segment, and the food
  disappears;
- if the head goes outside the board or collides with the body — the game ends.

The direction cannot be opposite to the current one.

**Requirements:**
- **R1.** The head moves one cell in the given direction.
- **R2.** Eating food increases the snake length by 1.
- **R3.** Colliding with a wall or the body ends the game.
- **R4.** The direction cannot be opposite to the current one.

**Logic.** New head = head + `direction`. Check bounds and collision. If the new
head == food → `grow`.

**Boundary cases:**
- Head within bounds, food on the path.
- Head on the tail (tail is released).
- 180° turn is forbidden.

**Invariants:**
- Without food, length is preserved.
- Segments do not overlap.
- Input is not modified.

---

### T19. Collision (snake)

**Signature:** `def collides(snake: list[tuple], head: tuple) -> bool`

**Description.** The function receives a list of snake segment coordinates and
head coordinates.

It checks whether the head coincides with any body segment.

The function returns `True` if the head coincides with at least one body
segment. Otherwise it returns `False`.

The head itself — the first segment — is not considered a collision.

**Requirements:**
- **R1.** `True` on coincidence with the body.
- **R2.** `False` if there is no coincidence.
- **R3.** Do not modify the input data.

**Logic.** Iterate over `snake[1:]`, check `head == segment`.

**Boundary cases:**
- Empty body → `False`.
- Head coincides with the tail → depends on the rules.

**Invariants:**
- Input is not modified.

---

### T20. Grow on eat (snake)

**Signature:** `def grow(state) -> state`

**Description.** The function receives the snake state.

It returns a new state in which the snake length is increased by one segment.
The new segment is added to the tail and repeats the position of the last
segment.

The other state fields are not modified.

**Requirements:**
- **R1.** Length increases by 1.
- **R2.** The new segment is added to the tail.
- **R3.** Other fields are not modified.
- **R4.** Do not modify the input state.

**Logic.** Duplicate the last segment.

**Boundary cases:**
- Snake with 1 segment → 2.
- Empty snake → error.

**Invariants:**
- Length +1.

---

### T21. Piece rotation (tetris)

**Signature:** `def rotate(piece: list[tuple]) -> list[tuple]`

**Description.** The function receives a list of cell coordinates of a tetris
piece.

It returns a new list of coordinates after rotating the piece 90° clockwise
around the origin.

The number of cells is unchanged.

**Requirements:**
- **R1.** 90° clockwise rotation.
- **R2.** The number of cells is preserved.
- **R3.** Four rotations return the original piece.
- **R4.** Do not modify the input list.

**Logic.** `(x, y) → (y, -x)`.

**Boundary cases:**
- 1 cell → unchanged.
- 4 rotations → original.

**Invariants:**
- The number of cells is preserved.
- Area is preserved.

---

### T22. Line clearing (tetris)

**Signature:** `def clear_lines(board) -> tuple[board, int]`

**Description.** The function receives a tetris board.

It removes all completely filled rows and shifts the upper rows down.

The function returns a tuple of two values:

- the new board;
- the number of removed rows.

The number of rows in the board is unchanged.

**Requirements:**
- **R1.** Remove all filled rows.
- **R2.** Shift upper rows down.
- **R3.** Return the number of removed rows.
- **R4.** The number of rows is unchanged.

**Logic.** Find filled rows. Remove them, shift upper rows, pad with empty rows.

**Boundary cases:**
- No filled rows → `(board, 0)`.
- All rows filled → `(empty, N)`.

**Invariants:**
- The number of rows is preserved.
- The order of remaining rows is preserved.

---

### T23. Position validity (tetris)

**Signature:** `def is_valid_position(board, piece, offset) -> bool`

**Description.** The function receives a tetris board, piece coordinates, and an
offset.

It checks whether the piece can be placed in the new position.

The function returns `True` if:

- all piece cells are within the board;
- the piece does not overlap with already occupied cells.

In all other cases, the function returns `False`.

**Requirements:**
- **R1.** `True` if all piece cells are within the board.
- **R2.** `True` if there is no overlap with occupied cells.
- **R3.** `False` in all other cases.
- **R4.** Do not modify the input data.

**Logic.** For each piece cell + `offset`: check bounds and occupancy.

**Boundary cases:**
- Partially outside the board → `False`.
- Overlap → `False`.

**Invariants:**
- Input is not modified.

---

### T24. Piece drop (tetris)

**Signature:** `def drop(board, piece) -> board`

**Description.** The function receives a tetris board and piece coordinates.

It returns a new board in which the piece is dropped to the maximum possible
height — until it collides with another piece or the bottom of the board.

The piece shape is not modified.

**Requirements:**
- **R1.** The piece drops until collision.
- **R2.** Shape is not modified.
- **R3.** A new board is returned.
- **R4.** Do not modify the input board.

**Logic.** While it can move down — move down.

**Boundary cases:**
- Piece already at the bottom → no changes.

**Invariants:**
- Shape is not modified.

---

### T25. Step (Conway's Game of Life)

**Signature:** `def step(grid: list[list[bool]]) -> list[list[bool]]`

**Description.** The function receives a Conway's Game of Life grid.

It returns a new grid after one step according to the B3/S23 rules:

- a live cell survives if it has 2 or 3 live neighbors;
- a dead cell becomes alive if it has exactly 3 live neighbors;
- other cells die or remain dead.

Board edges are not wrapped: neighbors outside the board are considered dead.

**Requirements:**
- **R1.** A live cell with 2 or 3 neighbors survives.
- **R2.** A dead cell with 3 neighbors becomes alive.
- **R3.** Other cells die or remain dead.
- **R4.** Edges are not wrapped.

**Logic.** For each cell: count neighbors, apply the B3/S23 rules.

**Boundary cases:**
- Empty board → empty.
- Blinker → returns after 2 steps.

**Invariants:**
- Size is preserved.
- Input is not modified.

---

### T26. Neighbors (Conway's Game of Life)

**Signature:** `def neighbors(grid, x: int, y: int) -> int`

**Description.** The function receives a grid and cell coordinates.

It returns the number of live neighbors (from 0 to 8). Neighbors are the 8
cells around the specified one. Cells outside the board are considered dead.

The cell itself is not counted.

**Requirements:**
- **R1.** Return the number of live neighbors (0–8).
- **R2.** Consider 8 cells around.
- **R3.** Cells outside the board are dead.
- **R4.** Do not count the cell itself.

**Logic.** For each of the 8 positions: if within bounds and alive → `count++`.

**Boundary cases:**
- Corner → 3 neighbors.
- Center → 8 neighbors.

**Invariants:**
- `0 ≤ result ≤ 8`.
- Input is not modified.

---

### T27. Pathfinding (map)

**Signature:** `def find_path(grid, start: tuple, end: tuple) -> list`

**Description.** The function receives a grid where `0` is a passable cell and
`1` is an obstacle. It also receives start and end coordinates.

It returns the shortest path from `start` to `end` as a list of coordinates,
including `start` and `end`. Movement is allowed only horizontally and
vertically. If there is no path, it returns an empty list.

**Requirements:**
- **R1.** Return the shortest path from `start` to `end`.
- **R2.** The path includes `start` and `end`.
- **R3.** Movement only horizontally and vertically.
- **R4.** Empty list if there is no path.

**Logic.** BFS from `start`. Visited cells. Path reconstruction via parents.

**Boundary cases:**
- No path → `[]`.
- `start == end` → `[start]`.
- Obstacles block the way.

**Invariants:**
- Path is shortest.
- Input is not modified.

---

### T28. Ship hit (battleship)

**Signature:** `def is_hit(board, x: int, y: int) -> bool`

**Description.** The function receives a 10×10 battleship board where each cell
contains `'S'` (ship), `'M'` (miss), `'H'` (hit), or `''` (empty), along with
shot coordinates.

It returns `True` if the cell contains a ship. It returns `False` if the cell is
empty, already shot at, or the coordinates are outside the board.

The function does not modify the board.

**Requirements:**
- **R1.** `True` if the cell is `'S'`.
- **R2.** `False` if the cell is empty or already shot at.
- **R3.** `False` if coordinates are out of bounds.
- **R4.** Do not modify the board.

**Logic.** Check bounds: `0 ≤ x, y ≤ 9`. `board[x][y] == 'S'`.

**Boundary cases:**
- Coordinates out of bounds → `False`.
- Cell `'M'` or `'H'` → `False`.
- Cell `'S'` → `True`.

**Invariants:**
- Input is not modified.

---

### T29. Ship sunk (battleship)

**Signature:** `def is_sunk(board, ship_id: int) -> bool`

**Description.** The function receives a 10×10 battleship board where ships are
labeled with numbers (1, 2, 3, …), hits are marked `'H'`, misses are `'M'`, and
empty cells are `''`.

It returns `True` if all cells of the ship with the given ID have been shot at
(marked `'H'`). It returns `False` if at least one cell of the ship has not been
shot at, or if no ship with that ID exists.

**Requirements:**
- **R1.** `True` if all ship cells are marked `'H'`.
- **R2.** `False` if at least one cell is not shot at.
- **R3.** `False` if no ship with that ID exists.
- **R4.** Do not modify the board.

**Logic.** Find all cells with `ship_id`. Check that all are `'H'`.

**Boundary cases:**
- Single-cell ship, shot at → `True`.
- 3-cell ship, 2 cells shot at → `False`.
- No ship with that ID → `False`.

**Invariants:**
- Input is not modified.

---

### T30. All ships sunk (battleship)

**Signature:** `def all_ships_sunk(board) -> bool`

**Description.** The function receives a 10×10 battleship board.

It returns `True` if all ships are sunk: all cells that originally contained
ships are marked `'H'`, and there is not a single `'S'` cell. It returns `False`
in all other cases.

**Requirements:**
- **R1.** `True` if there are no `'S'` cells.
- **R2.** `True` if all ships are marked `'H'`.
- **R3.** `False` if at least one `'S'` cell remains.
- **R4.** Do not modify the board.

**Logic.** Check for the absence of `'S'` on the board.

**Boundary cases:**
- Empty board (no ships) → `True`.
- One `'S'` remains → `False`.

**Invariants:**
- Input is not modified.

---

### T31. Move validity (reversi)

**Signature:** `def is_valid_reversi_move(board, x: int, y: int, color: str) -> bool`

**Description.** The function receives an 8×8 reversi board where cells contain
`'B'`, `'W'`, or `''`, move coordinates, and the player's color (`'B'` or
`'W'`).

It returns `True` if the move is valid: the cell is empty, and in at least one
of the 8 directions there is a continuous line of opponent pieces closed off by
the player's piece.

It returns `False` in all other cases.

**Requirements:**
- **R1.** `True` if the cell is empty.
- **R2.** `True` if at least one direction captures.
- **R3.** `False` if the cell is occupied.
- **R4.** `False` if no direction captures.

**Logic.** For each of the 8 directions: walk along the line, find opponent
pieces, check whether the line is closed off by the player's piece.

**Boundary cases:**
- Board corner.
- Cell on the edge.
- No opponent pieces nearby → `False`.

**Invariants:**
- Input is not modified.

---

### T32. Apply move (reversi)

**Signature:** `def apply_reversi_move(board, x: int, y: int, color: str) -> board`

**Description.** The function receives an 8×8 reversi board, move coordinates,
and the player's color.

It returns a new board after the move: the player's piece is placed on the
specified cell, and all opponent pieces that lie between the new piece and
another player's piece in any of the 8 directions are flipped to the player's
color.

If the move is invalid, it returns the original board unchanged.

**Requirements:**
- **R1.** Place the player's piece on the specified cell.
- **R2.** Flip all captured opponent pieces.
- **R3.** If the move is invalid — do not modify the board.
- **R4.** Do not modify the input board (return a new one).

**Logic.** For each direction: collect a line of opponent pieces; if it is closed
off by the player's piece — flip them.

**Boundary cases:**
- Move in a corner.
- Capture in multiple directions at once.
- Invalid move → no changes.

**Invariants:**
- The number of the player's pieces increases.
- Input is not modified.

---

### T33. Roll (dice)

**Signature:** `def roll_dice(n: int, rng) -> list[int]`

**Description.** The function receives the number of rolls and a random number
generator.

It returns a list of `n` integers in the range from 1 to 6. With a fixed
generator seed, the result is reproducible.

**Requirements:**
- **R1.** Return a list of length `n`.
- **R2.** All values are in the range `[1, 6]`.
- **R3.** Reproducibility with a fixed seed.
- **R4.** Do not modify `rng` outside of calls.

**Logic.** `[rng.randint(1, 6) for _ in range(n)]`.

**Boundary cases:**
- `n = 0` → `[]`.
- Fixed seed → reproducible.

**Invariants:**
- Length = `n`.
- All values ∈ `[1, 6]`.

---

### T34. Roll sum (dice)

**Signature:** `def roll_sum(n: int, rng) -> int`

**Description.** The function receives the number of rolls and a random number
generator.

It returns the sum of `n` dice rolls (each value from 1 to 6). With a fixed
seed, the result is reproducible.

**Requirements:**
- **R1.** Sum of `n` values in the range `[n, 6n]`.
- **R2.** Reproducibility with a fixed seed.
- **R3.** Do not modify `rng` outside of calls.

**Logic.** `sum(roll_dice(n, rng))`.

**Boundary cases:**
- `n = 0` → `0`.

**Invariants:**
- `n ≤ result ≤ 6n`.

---

### T35. Next move (fifteen puzzle)

**Signature:** `def next_move(board) -> int | None`

**Description.** The function receives a 4×4 fifteen puzzle board (numbers 1–15
and 0 for the empty cell).

It returns the number of the tile that should be moved to bring the board closer
to the solved state. The solved state is: 1, 2, 3, 4 in the first row, 5–8 in
the second, 9–12 in the third, and 13–15 with 0 in the fourth.

If the board is already solved, it returns `None`.

**Requirements:**
- **R1.** Return the tile number to move.
- **R2.** The tile must be adjacent to the empty cell.
- **R3.** `None` if the board is solved.
- **R4.** Do not modify the input board.

**Logic.** Find the tile that should be in the empty cell's position. If that
tile is adjacent — return it.

**Boundary cases:**
- Solved board → `None`.
- Tile not adjacent → choose another.

**Invariants:**
- Input is not modified.

---

### T36. Best move (tic-tac-toe)

**Signature:** `def best_move(board, player: str) -> tuple[int, int] | None`

**Description.** The function receives a 3×3 board and the player's symbol
(`'X'` or `'O'`).

It returns the coordinates `(row, col)` of the best move for this player: a move
that leads to a win, blocks the opponent's win, takes the center, or takes a
corner. If no moves are possible (the board is full), it returns `None`.

**Requirements:**
- **R1.** Return the coordinates of an empty cell.
- **R2.** Prefer a winning move.
- **R3.** Otherwise — a blocking move.
- **R4.** `None` if the board is full.

**Logic.** Check winning moves. Check blocking moves. Priority: center → corner
→ edge.

**Boundary cases:**
- Board full → `None`.
- Winning move exists → return it.

**Invariants:**
- Input is not modified.

---

## Group D. Utilities

### T37. Apply damage (HP / damage)

**Signature:** `def apply_damage(hp: int, damage: int) -> int`

**Description.** The function receives the current health and the amount of
damage.

It returns the new health: `hp` minus `damage`, but no less than 0. If `damage`
is negative, health is not modified.

The function has no side effects.

**Requirements:**
- **R1.** Return `max(0, hp - damage)`.
- **R2.** Negative damage does not modify `hp`.
- **R3.** Result ≥ 0.
- **R4.** No side effects.

**Logic.** `max(0, hp - damage)` when `damage > 0`.

**Boundary cases:**
- `hp=10, damage=15` → `0`.
- `hp=10, damage=-5` → `10`.

**Invariants:**
- Result ≥ 0.
- Monotonic in `damage`.

---

### T38. Level up (experience)

**Signature:** `def level_up(xp: int) -> int`

**Description.** The function receives the number of experience points.

It returns the player's level: level 1 for `xp` from 0 to 99, level 2 for
100–299, level 3 for 300–599, level 4 for 600–999, and so on (each level
requires 100 more points than the previous one). Negative `xp` is treated as 0.

**Requirements:**
- **R1.** Level 1 for `xp < 100`.
- **R2.** Each next level requires 100 more.
- **R3.** Negative `xp` = 0.
- **R4.** Monotonic in `xp`.

**Logic.** Thresholds: 100, 300, 600, 1000, … Formula: `n*(n+1)/2 * 100`.

**Boundary cases:**
- `xp = 0` → `1`.
- `xp = 99` → `1`.
- `xp = 100` → `2`.

**Invariants:**
- Monotonic.

---

### T39. Add item (inventory)

**Signature:** `def add_item(inv: dict, item: str, count: int) -> dict`

**Description.** The function receives an inventory (a dictionary item →
quantity), an item name, and a quantity.

It returns a new inventory with the added quantity. If the item already exists,
the quantity is summed. If `count ≤ 0`, the inventory is not modified.

**Requirements:**
- **R1.** Sum the quantity if the item already exists.
- **R2.** Add a new key if the item does not exist.
- **R3.** `count ≤ 0` does not modify the inventory.
- **R4.** Do not modify the input dictionary.

**Logic.** Copy `inv`. If `item` is in `inv` → sum, otherwise → new key.

**Boundary cases:**
- New item → `{item: count}`.
- `count = 0` → no changes.

**Invariants:**
- Input is not modified.
- Total quantity = original + `count`.

---

### T40. Total weight (inventory)

**Signature:** `def total_weight(inv: dict, weights: dict) -> int`

**Description.** The function receives an inventory (item → quantity) and a
weights dictionary (item → weight of one unit).

It returns the total weight of all items. Items missing from the weights
dictionary are ignored. An empty inventory gives 0.

**Requirements:**
- **R1.** Sum of `count × weight` for all items.
- **R2.** Ignore items without a weight.
- **R3.** Empty inventory → `0`.
- **R4.** Do not modify the input dictionaries.

**Logic.** `sum(count × weights[item] for item, count in inv.items() if item in weights)`.

**Boundary cases:**
- Empty inventory → `0`.
- Unknown item → ignore.

**Invariants:**
- Result ≥ 0.
- Input is not modified.