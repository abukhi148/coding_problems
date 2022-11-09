# https://jutge.org/problems/P77686_en/statement


def is_palindromic(n):
    return str(n) == str(n)[::-1]
