# https://jutge.org/problems/P37469_en
t = int(input())
h, m, s = t // 3600, (t % 3600) // 60, (t % 3600) % 60
print(h, m, s)
