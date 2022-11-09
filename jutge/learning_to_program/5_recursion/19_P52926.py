# https://jutge.org/problems/P52926_en
import sys

names = [x for x in sys.stdin.read().rsplit("\n") if x]
for i in names[: names.index("end")][::-1]:
    print(i)
