# https://jutge.org/problems/P80660_en
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit("\n") if x]
for n in numbers:
    m = 0
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        m += 1
    print(m)
