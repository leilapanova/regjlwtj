def divide_list(lst):
    half = len(lst) // 2
    first_half = lst[:half]
    second_half = lst[half:]

    sum_first_half = sum(first_half)
    sum_second_half = sum(second_half)

    result = sum_first_half / sum_second_half
    return result