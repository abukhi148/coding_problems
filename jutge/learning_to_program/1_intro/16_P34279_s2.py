# https://jutge.org/problems/P34279_en
h, m, s = tuple(map(int, input().rsplit()))
s += 1
if s == 60:
    s = 0
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
t = [str(x).zfill(2) for x in [h, m, s]]
print(f"{t[0]}:{t[1]}:{t[2]}")
