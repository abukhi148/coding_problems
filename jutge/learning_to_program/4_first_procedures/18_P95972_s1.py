# https://jutge.org/problems/P95972_en/statement

import math


def sum_divisors(n):
    d = [1, n]
    [d.extend([i, n / i]) for i in range(2, int(math.sqrt(n)) + 1) if n % i == 0]
    return int(sum(list(set(d))))
