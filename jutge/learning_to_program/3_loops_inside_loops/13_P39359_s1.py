# https://jutge.org/problems/P39359_en/statement
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit("\n") if len(x) > 0]
s = "0123456789"
n = sum([n * n for n in numbers])
y = s * (n // len(s)) + s[: n % len(s)]
r = list()
start = 0
for i in range(len(numbers)):
    x = ""
    end = start + numbers[i] * numbers[i]
    s1 = y[start:end]
    [
        x := x + s1[numbers[i] * j : numbers[i] * j + numbers[i]] + "\n"
        for j in range(0, numbers[i])
    ]
    r.append(x)
    start = end
print(*r, sep="\n", end="")
