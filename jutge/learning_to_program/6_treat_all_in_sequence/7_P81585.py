# https://jutge.org/problems/P81585_en

import sys

s = [int(x) for x in sys.stdin.read().split() if x]
while s:
    l, s = s[1 : s[0] + 1], s[s[0] + 1 :]
    print("YES") if sum(l) - max(l) == max(l) else print("NO")
