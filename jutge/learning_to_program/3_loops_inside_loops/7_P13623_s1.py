# https://jutge.org/problems/P13623_en
import sys

r, c = tuple(map(int, input().rsplit()))
numbers = [[int(y) for y in x] for x in sys.stdin.read().rsplit("\n") if len(x) > 0]
total = 0
for x in range(1, c + 1):
    for y in range(1, r + 1):
        if x % 2 != 0 and y % 2 != 0:
            total = total + numbers[y - 1][x - 1]
        elif x % 2 == 0 and y % 2 == 0:
            total = total + numbers[y - 1][x - 1]
print(total)
