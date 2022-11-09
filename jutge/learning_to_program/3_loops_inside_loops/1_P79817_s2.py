# https://jutge.org/problems/P79817_en
import sys

[
    print(number**power)
    for number, power in [
        tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if len(x) > 1
    ]
]
