# https://jutge.org/problems/P24080_en/statement
import sys

numbers = [int(x) for x in sys.stdin.read().rsplit()]
r = [f"{str(n) * n}\n" * n for n in numbers]
print(*r, sep="\n", end="")
