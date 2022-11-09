# https://jutge.org/problems/P12061_en
import sys

s = sys.stdin.readline().split()
start, end = False, False
c = 0
while s:
    if s[0] == "beginning":
        start = True
    elif start and s[0] == "end":
        end = True
        break
    elif start:
        c += 1
    s = s[1:]
print(c if start and end else "wrong sequence")
