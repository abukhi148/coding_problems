# https://jutge.org/problems/P39057_en/statement
import math

descriptions = int(input())
results = []
for i in range(descriptions):
    figure = input().rsplit()
    if figure[0] == "rectangle":
        area = float(figure[1]) * float(figure[2])
        results.append("{:.6f}".format(area))
    elif figure[0] == "circle":
        area = math.pi * float(figure[1]) ** 2
        results.append("{:.6f}".format(area))

for i in results:
    print(i)
