# https://jutge.org/problems/P26041_en
import sys

names = [x for x in sys.stdin.read().rsplit("\n") if x][::-1]
for i in names:
    print(i)
