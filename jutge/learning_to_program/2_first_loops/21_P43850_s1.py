# https://jutge.org/problems/P43850_en
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit()]
for number in numbers:
    x = 1 / 5 * (1 / 4 * (number / 5 - 9) - 6)
    print("{:.0f}".format(x))
