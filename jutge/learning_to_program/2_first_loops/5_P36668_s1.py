# https://jutge.org/problems/P36668_en/statement
n = int(input())
sum_n = 0
for i in range(1, n + 1):
    sum_n = sum_n + i**2
print(sum_n)
