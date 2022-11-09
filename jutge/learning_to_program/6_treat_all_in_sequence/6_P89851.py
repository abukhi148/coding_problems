# https://jutge.org/problems/P89851_en

import re
import sys

s = sys.stdin.read()
s = [list(map(int, i.split())) for i in re.split(r"\n", s) if s]
for i in s:
    for n in list(range(1, i[0] + 1)):
        if n not in i[1:]:
            print(n)
            break
