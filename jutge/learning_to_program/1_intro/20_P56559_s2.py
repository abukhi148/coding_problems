# https://jutge.org/problems/P56559_en/statement
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))
print("=") if a1 == a2 and b1 == b2 else (
    print("1")
    if (a2 <= a1 <= b2) and (a2 <= b1 <= b2)
    else (print("2") if (a1 <= a2 <= b1) and (a1 <= b2 <= b1) else print("?"))
)
