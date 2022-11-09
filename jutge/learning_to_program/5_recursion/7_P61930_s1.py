# https://jutge.org/problems/P61930_en


def sum_of_digits(x):
    return x if x < 10 else sum_of_digits(x // 10) + x % 10


def is_multiple_3(x):
    return x in [3, 6, 9] if x < 10 else is_multiple_3(sum_of_digits(x))
