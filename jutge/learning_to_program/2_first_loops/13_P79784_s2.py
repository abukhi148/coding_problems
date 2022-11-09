# https://jutge.org/problems/P79784_en
import sys

s = sys.stdin.read()
x, y = 0, 0
[
    (
        x := x + 1 if i == "e" else (x - 1 if i == "w" else x),
        y := y + 1 if i == "s" else (y - 1 if i == "n" else y),
    )
    for i in s
    if s
]
print((x, y))
# TODO: WTF!
