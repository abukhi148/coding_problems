# https://jutge.org/problems/P96767_en
x = float(input())
polynomial = list(map(float, input().rsplit()))
result = 0
for i in range(len(polynomial)):
    result = result + polynomial[i] * x**i
print("{:.4f}".format(result))
