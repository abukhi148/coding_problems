# https://jutge.org/problems/P59875_en
a, b = tuple(map(int, input().rsplit()))
[print(i) for i in [x for x in range(min(a, b), max(a, b) + 1)][::-1]]
