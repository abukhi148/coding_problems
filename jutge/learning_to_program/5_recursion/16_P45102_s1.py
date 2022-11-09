# https://jutge.org/problems/P45102_en
import operator


def apply_op(o, a, b):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    return ops[o](a, b)


def solve(i=0):
    if d[i] in ["+", "-", "*"]:
        return d[i], i + 1
    elif d[i].isdigit():
        return int(d[i]), i + 1
    elif d[i] == ")":
        return solve(i + 1)
    else:
        i += 1
        n1, i = solve(i)
        op, i = solve(i)
        n2, i = solve(i)
        return apply_op(op, n1, n2), i


d = list(input().split())
print(solve()[0])
