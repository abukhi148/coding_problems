# https://jutge.org/problems/P92998_en
import sys

names = [x for x in sys.stdin.read().rsplit("\n") if x]
for i in names[1 : int(names[0]) + 1][::-1]:
    print(i)
