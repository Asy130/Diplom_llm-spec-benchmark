def merge_row(row):
    non_zero = [x for x in row if x != 0]
    result = []
    i = 0
    while i < len(non_zero):
        if i + 1 < len(non_zero) and non_zero[i] == non_zero[i+1]:
            result.append(non_zero[i] * 2)
            i += 2 # Skip both merged tiles
        else:
            result.append(non_zero[i])
            i += 1
    result.extend([0] * (len(row) - len(result)))
    return result