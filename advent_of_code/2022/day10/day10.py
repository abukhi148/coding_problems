from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=10, year=year)


def parse(data):
    data = [
        int(i[1]) if i[0] != "noop" else 0
        for i in (i.split() for i in data.splitlines())
    ]
    return data


def p1(data):
    x, c = 1, 1
    r = list()
    cs = [20, 60, 100, 140, 180, 220]
    for i in data:
        if i != 0:
            c += 2
            x += i
        else:
            c += 1
        if cs:
            if c in cs:
                r.append(c * x)
                cs.pop(0)
            elif c - 1 in cs:
                r.append((c - 1) * (x - i))
                cs.pop(0)
    return sum(r)


# TODO: cant figure out how to implement this
def p2(data):
    crt = [0] * 40
    x, cycle = 1, 1, 1
    for i in data:
        cycle += 1 if i == 0 else 2
        x += i
        if x <= cycle - 1 <= x + 3:
            crt[x - 1] = 1
    print(crt)


data = parse(p.input_data)
submit(p1(data), part="a", day=10, year=year)
# p2(data)
# submit(p2(p.input_data), part="b", day=day, year=year)
