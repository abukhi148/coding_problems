# https://jutge.org/problems/P37469_en
time = int(input())
h = time // 3600
m = (time % 3600) // 60
s = (time % 3600) % 60
print(h, m, s)
