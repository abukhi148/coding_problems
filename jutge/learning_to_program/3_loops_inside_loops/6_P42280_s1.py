# https://jutge.org/problems/P42280_en
import sys

r, c = tuple(map(int, input().rsplit()))
numbers = [x for x in sys.stdin.read().rsplit("\n") if len(x) > 0]
total = 0
if len(numbers) == r:
    for number in numbers:
        if len(number) == c:
            for i in number:
                total = total + int(i)
print(total)
