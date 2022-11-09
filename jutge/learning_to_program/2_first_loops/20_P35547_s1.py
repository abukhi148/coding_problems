# https://jutge.org/problems/P35547_en/statement
import sys

import math
import sys

years = [int(x) for x in sys.stdin.read().rsplit() if len(x) > 1]
for y in years:
    k = y // 100
    x = y % 19
    b = y % 4
    c = y % 7
    q = k // 4
    p = (13 + 8 * k) // 25
    y = (15 - p + k - q) % 30
    z = (19 * x + y) % 30
    n = (4 + k - q) % 7
    e = (2 * b + 4 * c + 6 * z + n) % 7
    if z + e <= 9:
        d = 22 + z + e
        m = 3
    elif z == 29 and e == 6:
        d = 19
        m = 4
    elif z == 28 and e == 6 and x > 10:
        d = 18
        m = 4
    else:
        d = z + e - 9
        m = 4
    print(f"{math.floor(d)}/{m}")
