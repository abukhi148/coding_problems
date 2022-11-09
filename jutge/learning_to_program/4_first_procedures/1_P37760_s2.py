# https://jutge.org/problems/P37760_en
import sys
import math

angles = [float(x) for x in sys.stdin.read().rsplit("\n") if x]
[
    print(
        "{:.6f}".format(math.sin(angle * math.pi / 180)),
        "{:.6f}".format(math.cos(angle * math.pi / 180)),
    )
    for angle in angles
]
