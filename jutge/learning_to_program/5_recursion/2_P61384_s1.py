# https://jutge.org/problems/P61384_en


def double_factorial(n):
    return 1 if n == 1 or n == 0 else n * double_factorial(n - 2)
