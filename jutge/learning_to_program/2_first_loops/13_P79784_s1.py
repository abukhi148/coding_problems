# https://jutge.org/problems/P79784_en
import sys

s = sys.stdin.read()
coordinates = [0, 0]
if len(s) > 0:
    for i in s:
        if i == "e":
            coordinates[0] = coordinates[0] + 1
        elif i == "w":
            coordinates[0] = coordinates[0] - 1
        elif i == "s":
            coordinates[1] = coordinates[1] + 1
        elif i == "n":
            coordinates[1] = coordinates[1] - 1
print(tuple(coordinates))
