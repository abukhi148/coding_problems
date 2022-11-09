# https://jutge.org/problems/P34091_en/statement
import math


def is_perfect(n):
    d = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d.extend([i, n // i] if i ** 2 != n else [i])
    print(sum(d))
    return sum(d) == n


is_perfect(49)
# TODO: revise
