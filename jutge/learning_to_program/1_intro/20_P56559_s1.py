# https://jutge.org/problems/P56559_en/statement
a1, b1, a2, b2 = tuple(map(int, input().rsplit()))
if a1 == a2 and b1 == b2:
    print("=")
elif (a2 <= a1 <= b2) and (a2 <= b1 <= b2):
    print("1")
elif (a1 <= a2 <= b1) and (a1 <= b2 <= b1):
    print("2")
else:
    print("?")
