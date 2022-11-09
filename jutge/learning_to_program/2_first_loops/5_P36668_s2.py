# https://jutge.org/problems/P36668_en/statement
s = 0
[s := s + i**2 for i in range(1, int(input()) + 1)]
print(s)
