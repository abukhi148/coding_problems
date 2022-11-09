# https://jutge.org/problems/P51222_en


def number_of_digits(n, c=0):
    c += 1
    n = str(n)[1:]
    return c if n == "" else number_of_digits(n, c)
