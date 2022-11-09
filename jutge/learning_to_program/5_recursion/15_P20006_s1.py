# https://jutge.org/problems/P20006_en
import operator


def apply_op(o, a, b):
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    return ops[o](a, b)


def pre_ex(i=0):
    print(i, d[i], d)
    if d[i].isdigit():
        return int(d[i]), i + 1
    op, i = d[i], i + 1
    l, i = pre_ex(i)
    r, i = pre_ex(i)
    return apply_op(op, l, r), i


d = list(input().rsplit())
print(pre_ex()[0])
