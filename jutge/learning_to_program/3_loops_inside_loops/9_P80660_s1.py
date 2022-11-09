# https://jutge.org/problems/P80660_en
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit("\n") if len(x) > 0]

for n in numbers:
    m = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        m = m + 1
    print(m)
