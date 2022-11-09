# https://jutge.org/problems/P17913_en/statement


def double_factorial(n):
    product = 1
    [product := product * i for i in range(n, 0, -2)]
    return product
