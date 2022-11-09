# https://jutge.org/problems/P58153_en
from math import log


def H(n):
    if n == 0:
        return 0
    gamma = 0.57721566490153286060651209008240243104215933593992
    return (
        gamma
        + log(n)
        + 0.5 / n
        - 1.0 / (12 * n**2)
        + 1.0 / (120 * n**4)
        - 1.0 / (252 * n**6)
        + 1.0 / (240 * n**8)
        - 1.0 / (132 * n**10)
        + 691.0 / (32760 * n**12)
        - 1.0 / (12 * n**14)
        + 3617 / (8160 * n**16)
    )


r = []
i = input().rsplit("\n")[0]
while i != "":
    n, m = tuple(map(int, i.rsplit()))
    if n >= 1000000 or m >= 1000000:
        hm = round(H(m), 10)
        hn = round(H(n), 10)
    else:
        hn = sum((1 / i) for i in range(1, n + 1))
        hm = sum((1 / i) for i in range(1, m + 1))
    r.append("{:.10f}".format(hn - hm))
    i = input().rsplit("\n")[0]
print(*r, sep="\n")
