# https://jutge.org/problems/P43557_en/statement
from math import floor, sqrt


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = floor(sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


# Todo: make changes


def is_perfect_prime(n):
    p = is_prime(n)
    if len(str(n)) == 1 or not p:
        return p
    else:
        return is_perfect_prime(sum(list(map(int, list(str(n))))))
