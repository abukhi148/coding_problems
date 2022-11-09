# https://jutge.org/problems/P69277_en
n = int(input())
l = [x**3 for x in range(n + 1)]
print(*l, sep=",")
