# https://jutge.org/problems/P18203_en
import sys


def main(data):
    for n in data:
        if 0 in n:
            return f"0^3 + 0^3 = 0^3"
        else:
            for x in range(n[0], n[1] + 1):
                for y in range(n[2], n[3] + 1):
                    pow_sum = pow(x, 3) + pow(y, 3)
                    z = int(pow(pow_sum, 1.0 / 3))
                    z_pow = pow(z, 3)
                    if pow_sum == z_pow:
                        return f"{x}^3 + {y}^3 = {z}^3"
    return "No solution!"


print(main(sorted([tuple(map(int, i.split())) for i in sys.stdin.readlines()])))
