# https://jutge.org/problems/P39057_en/statement
import math

des = int(input())
r = []
for d in range(des):
    f = input().rsplit()
    r.append("{:.6f}".format(float(f[1]) * float(f[2]))) if f[0] == "rectangle" else (
        r.append("{:.6f}".format(math.pi * float(f[1]) ** 2))
    )
[print(i) for i in r]
