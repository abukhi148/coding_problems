# https://jutge.org/problems/P35537_en


def is_increasing(n, r=True):
    n = str(n)
    return (
        r
        if (n[0] == n[-1] and n[1:] == "") or r is False
        else is_increasing(n[1:], n[0:1] <= n[1:2])
    )
