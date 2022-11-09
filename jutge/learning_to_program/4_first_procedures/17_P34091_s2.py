# https://jutge.org/problems/P34091_en/statement


def is_perfect(n):
    mp = [
        3,
        7,
        31,
        127,
        8191,
        131071,
        524287,
        2147483647,
        2305843009213693951,
        618970019642690137449562111,
    ]
    s = 1
    i = n
    while s < n:
        i /= 2
        s += i
        if i % 2 != 0 and i in mp and ((i + 1) / 2 * i) == n:
            return True
    return False
