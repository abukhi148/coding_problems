# https://jutge.org/problems/P88790_en


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
