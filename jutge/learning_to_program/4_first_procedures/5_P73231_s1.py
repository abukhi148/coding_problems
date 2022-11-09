# https://jutge.org/problems/P73231_en


def max4(a, b, c, d):
    max_n = a
    [max_n := n for n in [a, b, c, d] if n >= max_n]
    return max_n
