# https://jutge.org/problems/P19991_en
import sys

n = int(input())
numbers = [list(map(int, list(x))) for x in sys.stdin.read().rsplit("\n") if x]
total = 0
[
    total := total + numbers[y][x]
    for y in range(n)
    for x in range(n)
    if (x == y) or (x + y == n - 1)
]
print(total)
