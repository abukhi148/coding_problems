# https://jutge.org/problems/P22467_en
import math


# TODO: make it recursive
def sum_digits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def is_prime(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i) == 0:
                return False
        return True
    return False


def is_perfect_prime(n):
    p = is_prime(n)
    if len(str(n)) == 1 or not p:
        return p
    else:
        return is_perfect_prime(sum_digits(n))
