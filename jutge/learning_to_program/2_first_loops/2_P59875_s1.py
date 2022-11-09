# https://jutge.org/problems/P59875_en
a, b = tuple(map(int, input().rsplit()))
start = min(a, b)
end = max(a, b) + 1
l = [x for x in range(start, end)]
l.reverse()
for i in l:
    print(i)
