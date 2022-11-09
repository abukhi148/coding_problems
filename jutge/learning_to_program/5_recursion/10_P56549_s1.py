# https://jutge.org/problems/P56549_en

import sys


def deci_2_bin(d, b=""):
    if d > 1:
        return deci_2_bin(d // 2, b + str(d % 2))
    else:
        return (b + "1" if d == 1 else b + "0")[::-1]


def deci_2_oct(d, o=""):
    if d > 0:
        return deci_2_oct(d // 8, o + str(d % 8))
    else:
        return "0" if not o else o[::-1]


def deci_2_hex(d, h=""):
    c = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    if d > 0:
        return deci_2_hex(d // 16, h + c[d % 16])
    else:
        return "0" if not h else h[::-1]


for i in [int(x) for x in sys.stdin.read().rsplit("\n") if x]:
    print(f"{i} = {deci_2_bin(i)}, {deci_2_oct(i)}, {deci_2_hex(i)}")
