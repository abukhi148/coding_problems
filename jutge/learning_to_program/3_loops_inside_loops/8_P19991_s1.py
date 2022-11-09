# https://jutge.org/problems/P19991_en
import sys

n = int(input())
numbers = [[int(y) for y in x] for x in sys.stdin.read().rsplit("\n") if len(x) > 0]
total = 0
for x in range(n):
    for y in range(n):
        if (x == y) or (x + y == n - 1):
            total = total + numbers[y][x]
print(total)
