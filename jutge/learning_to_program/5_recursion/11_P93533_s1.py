# https://jutge.org/problems/P93533_en
import sys


def deci_n_base2(n, b=""):
    if n != 0:
        n, r = divmod(n, -2)
        return (
            deci_n_base2(n + 1, b + str(abs(r)))
            if r < 0
            else deci_n_base2(n, b + str(r))
        )
    else:
        return "0" if not b else b[::-1]


for i in [int(x) for x in sys.stdin.read().rsplit("\n") if x]:
    print(f"{i}: {deci_n_base2(i)}")
