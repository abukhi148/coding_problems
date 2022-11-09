# https://jutge.org/problems/P33839_en/statement

import sys

[
    print(f"The sum of the digits of {n} is {sum(list(map(int, list(n))))}.")
    for n in sys.stdin.read().rsplit("\n")
    if n
]
