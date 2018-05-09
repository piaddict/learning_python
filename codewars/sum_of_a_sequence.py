def sequence_sum(begin_number, end_number, step):
    result = 0
    for i in range(begin_number, end_number + 1, step):
        result += i
    return result
