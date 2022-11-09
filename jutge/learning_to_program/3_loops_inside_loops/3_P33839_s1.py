# https://jutge.org/problems/P33839_en/statement

import sys

numbers = [x for x in sys.stdin.read().rsplit("\n") if len(x) >= 1]
for number in numbers:
    addition = 0
    for i in number:
        addition = addition + int(i)
    print(f"The sum of the digits of {number} is {addition}.")
