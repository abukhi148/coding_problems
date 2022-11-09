# https://jutge.org/problems/P34279_en
time = input().rsplit()
h, m, s = tuple(map(int, time))
s = s + 1
if s == 60:
    s = 0
    m = m + 1
    if m == 60:
        m = 0
        h = h + 1
        if h == 24:
            h = 0
h = str(h).zfill(2)
m = str(m).zfill(2)
s = str(s).zfill(2)

print(f"{h}:{m}:{s}")
