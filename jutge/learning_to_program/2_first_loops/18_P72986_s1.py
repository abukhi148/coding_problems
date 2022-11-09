# https://jutge.org/problems/P72986_en
x = float(input())
polynomial = list(map(float, input().rsplit()))[::-1]
result = 0
for i in range(len(polynomial)):
    result = result + polynomial[i] * x**i
print("{:.4f}".format(result))
