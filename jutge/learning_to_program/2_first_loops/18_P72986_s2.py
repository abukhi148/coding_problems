# https://jutge.org/problems/P72986_en
x, p = float(input()), list(map(float, input().rsplit()))[::-1]
r = 0
[r := r + p[i] * x**i for i in range(len(p))]
print("{:.4f}".format(r))
