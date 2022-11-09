# https://jutge.org/problems/P51126_en
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))
l = list()
print(l) if a2 > b1 or a1 > b2 else (
    l.append(max(a1, a2)),
    l.append(min(b1, b2)),
    print(str(l).replace(" ", "")),
)
