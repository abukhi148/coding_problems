# https://jutge.org/problems/P34080_en/statement
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit("\n") if x]
s = "0123456789"
r = list()
for n in numbers:
    x = ""
    y = s * (n * n // len(s)) + s[: n * n % len(s)]
    [x := x + str(y[n * i : n * i + n] + "\n") for i in range(0, n)]
    r.append(x)
print(*r, sep="\n", end="")
