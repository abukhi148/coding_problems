# https://jutge.org/problems/P29253_en
import sys

n_ro = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

r_nums = [list(x[:-1]) for x in sys.stdin.read().split() if x]
for r in r_nums:
    l, n = [n_ro[i] for i in r], list()
    while l:
        if len(l) == 1 or l[0] > l[1]:
            n.append(l.pop(0))
        elif l[0] < l[1]:
            n.append(abs(l.pop(0) - l.pop(0)))
        else:
            n.append(l.pop(0) + l.pop(0))
    print(f"{''.join(r)} = {sum(n)}")
