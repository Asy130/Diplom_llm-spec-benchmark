def check_preconditions(row):
    # LLM проверила типы и длину
    assert isinstance(row, list)
    assert len(row) == 9
    assert all(isinstance(x, int) and 0 <= x <= 9 for x in row)

def check_postconditions(row, result):
    # LLM проверила, что результат - булево значение
    assert isinstance(result, bool)