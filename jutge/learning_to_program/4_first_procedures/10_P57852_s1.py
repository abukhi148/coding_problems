# https://jutge.org/problems/P57852_en/statement


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def gcd4(a, b, c, d):
    n1, n2 = gcd(a, b), gcd(c, d)
    return gcd(n1, n2)
