# https://jutge.org/problems/P12509_en


def factorial(n):
    return 1 if n == 1 or n == 0 else n * factorial(n - 1)
