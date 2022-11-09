# https://jutge.org/problems/P37257_en


def three_equal_consecutive_digits(n, b, v=None, i=1):
    if n > 0 and i < 3:
        nv = n % b
        i = i + 1 if nv == v else 1
        return three_equal_consecutive_digits(n // b, b, nv, i)
    else:
        return i >= 3
