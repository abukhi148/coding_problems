# https://jutge.org/problems/P51126_en
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))
l = list()
if a2 > b1 or a1 > b2:
    print(l)
else:
    lower = max(a1, a2)
    upper = min(b1, b2)
    l.append(lower)
    l.append(upper)
    print(str(l).replace(" ", ""))
