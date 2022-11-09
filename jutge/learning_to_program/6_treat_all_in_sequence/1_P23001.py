# https://jutge.org/problems/P23001_en

s = input().split()
c, c_max = 0, 0
for i in s:
    if i == s[0]:
        c = c + 1
        c_max = c if c > c_max else c_max
    else:
        c = 0
print(c_max)
