# https://jutge.org/problems/P73501_en
n = int(input())
l, i = list(), 0
while i < n:
    seq = list(map(int, input().split()))
    s0, m = seq[0], 0
    for s in seq[1:]:
        m = m + 1 if s > s0 else m
        s0 = s
    l.append(m)
    i += 1
for x in l:
    print(x)
