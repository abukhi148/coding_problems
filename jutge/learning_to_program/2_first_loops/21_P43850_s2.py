# https://jutge.org/problems/P43850_en
import sys

[
    print("{:.0f}".format(1 / 5 * (1 / 4 * (n / 5 - 9) - 6)))
    for n in [int(x) for x in sys.stdin.read().rsplit()]
]
