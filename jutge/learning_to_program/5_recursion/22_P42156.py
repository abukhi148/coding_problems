# https://jutge.org/problems/P42156_en
import sys

names = [x for x in sys.stdin.read().rsplit("\n") if x]
for i in names[-len(names) // 2 :][::-1]:
    print(i)
