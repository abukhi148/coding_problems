# https://jutge.org/problems/P97156_en
(
    a,
    b,
) = tuple(map(int, input().rsplit()))
print(*range(a, b + 1), sep=",")
