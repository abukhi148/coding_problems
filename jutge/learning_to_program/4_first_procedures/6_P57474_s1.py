# https://jutge.org/problems/P57474_en


def factorial(n):
    product = 1
    [product := product * i for i in range(1, n + 1)]
    return product
