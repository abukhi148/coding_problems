# https://jutge.org/problems/P89265_en
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))

l = list()
if a2 > b1 or a1 > b2:
    pass
else:
    lower = max(a1, a2)
    upper = min(b1, b2)
    l.append(lower)
    l.append(upper)

type1 = "?"
if a1 == a2 and b1 == b2:
    type1 = "="
elif (a2 <= a1 <= b2) and (a2 <= b1 <= b2):
    type1 = "1"
elif (a1 <= a2 <= b1) and (a1 <= b2 <= b1):
    type1 = "2"

print(f'{type1} , {str(l).replace(" ", "")}')
