# https://jutge.org/problems/P89265_en
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))
l = list()
l if (a2 > b1 or a1 > b2) else (l.append(max(a1, a2)), l.append(min(b1, b2)))
t = (
    "="
    if a1 == a2 and b1 == b2
    else (
        "1"
        if (a2 <= a1 <= b2) and (a2 <= b1 <= b2)
        else ("2" if (a1 <= a2 <= b1) and (a1 <= b2 <= b1) else ("?"))
    )
)
print(f'{t} , {str(l).replace(" ", "")}')
