def merge_row(row):
    non_zero = [x for x in row if x != 0]
    result = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i+1]:
            result.append(non_zero[i] * 2)
            i += 1 # BUG: Should be i += 2
        else:
            result.append(non_zero[i])
        i += 1
    result.extend([0] * (len(row) - len(result)))
    return result

# COUNTEREXAMPLE (Proves this is faulty):
# Input: [2, 2, 2, 2]
# Expected: [4, 4, 0, 0] (each tile merges only once)
# Actual: [4, 2, 2, 0] (merging logic fails on consecutive equal tiles)