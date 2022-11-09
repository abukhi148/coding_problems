# https://jutge.org/problems/P36430_en


def main(n):
    if 0 in n:
        return f"0^2 + 0^2 = 0^2"
    else:
        for x in range(n[0], n[1] + 1):
            for y in range(n[2], n[3] + 1):
                pow_sum = pow(x, 2) + pow(y, 2)
                z = int(pow(pow_sum, 1.0 / 2))
                z_pow = pow(z, 2)
                if pow_sum == z_pow:
                    return f"{x}^2 + {y}^2 = {z}^2"
        return "No solution!"


n = tuple(map(int, input().split()))
print(main(n))
# todo: revise later
