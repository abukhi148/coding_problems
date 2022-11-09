# https://jutge.org/problems/P96564_en/statement
from math import gcd
import sys

numbers = [list(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if x]
for n in numbers:
    if n[0] > 0:
        a = n[1:]
        lcm = 1
        [lcm := lcm * i // gcd(lcm, i) for i in a]
        print(lcm)
