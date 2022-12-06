from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)


def p1(data):
    r = ""
    for i, c in enumerate(data):
        if len(r) < 4:
            if c in r:
                r = r[r.index(c) + 1 :]
            r += c
        else:
            break
    return i


def p2(data):
    r = ""
    for i, c in enumerate(data):
        if len(r) < 14:
            if c in r:
                r = r[r.index(c) + 1 :]
            r += c
        else:
            break
    return i


submit(p1(p.input_data), part="a", day=day, year=year)
submit(p2(p.input_data), part="b", day=day, year=year)
