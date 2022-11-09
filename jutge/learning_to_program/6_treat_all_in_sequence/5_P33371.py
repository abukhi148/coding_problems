# https://jutge.org/problems/P33371_en

import string
import sys

alphabets = list(string.ascii_lowercase)


def encoded(c, k):
    s = ""
    for i in c:
        if i in alphabets:
            idx = (alphabets.index(i) + k) % 26
            i = alphabets[idx].upper()
        s += i
    return s.replace("_", " ")[:-1]


l = sys.stdin.read().split()
l = list(zip(l[0::2], l[1::2]))
for k, c in l:
    print(encoded(c, int(k)))
