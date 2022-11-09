# https://jutge.org/problems/P79817_en
import sys

numbers = [
    tuple(map(int, x.rsplit())) for x in sys.stdin.read().rsplit("\n") if len(x) > 1
]
for number, power in numbers:
    print(number**power)
