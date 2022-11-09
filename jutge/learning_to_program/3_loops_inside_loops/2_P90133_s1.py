# https://jutge.org/problems/P90133_en
import sys

numbers = [tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if x]
for b, n in numbers:
    c = 0
    while n > 1:
        n /= b
        c += 1
    if n < 1:
        c -= 1
    print(c)
