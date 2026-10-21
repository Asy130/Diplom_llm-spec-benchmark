def is_valid_row(row):
    seen = set()
    for num in row:
        if num != 0:
            if num in seen:
                return False
            seen.add(num)
    return True