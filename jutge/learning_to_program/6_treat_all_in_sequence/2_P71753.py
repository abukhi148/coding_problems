# https://jutge.org/problems/P71753_en

import sys

nl = [int(x) for x in sys.stdin.read().split() if x]
while nl:
    l, nl = nl[1 : nl[0] + 1], nl[nl[0] + 1 :]
    m = l[0]
    for i in l[1:]:
        m = i if i > m else m
    print(m)
