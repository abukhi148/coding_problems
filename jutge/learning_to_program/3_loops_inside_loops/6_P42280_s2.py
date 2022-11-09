# https://jutge.org/problems/P42280_en
import sys

r, c = tuple(map(int, input().rsplit()))
numbers = [list(map(int, list(x))) for x in sys.stdin.read().rsplit("\n") if x]
s = 0
[s := s + sum(n) for n in numbers] if (
    len(numbers) == r and len(numbers[0]) == c
) else None
print(s)
