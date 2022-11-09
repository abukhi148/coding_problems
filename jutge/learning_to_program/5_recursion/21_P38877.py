# https://jutge.org/problems/P38877_en
import sys

names = [x for x in sys.stdin.read().rsplit("\n") if x]
n = int(names.pop(0))
for i in names[::-1][:n]:
    print(i)
