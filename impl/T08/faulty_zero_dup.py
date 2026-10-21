def is_valid_row(row):
    seen = set()
    for num in row:
        if num in seen: # BUG: Doesn't check if num == 0
            return False
        seen.add(num)
    return True

# COUNTEREXAMPLE (Proves this is faulty):
# Input: [0, 0, 0, 0, 0, 0, 0, 0, 0]
# Expected: True (empty cells are allowed)
# Actual: False (it sees the second 0 as a duplicate)