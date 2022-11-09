# https://jutge.org/problems/P38045_en

import sys

numbers = [float(x) for x in sys.stdin.read().rsplit("\n") if x]
[
    print("{:.0f}".format(number**2), "{:.6f}".format(number ** (1 / 2)))
    for number in numbers
]
