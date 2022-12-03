from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)


def p1(data):
    data = [(i[: len(i) // 2], i[len(i) // 2 :]) for i in data.splitlines()]
    s = 0
    for c1, c2 in data:
        for i in c1:
            if i in c2:
                if i.isupper():
                    s += ord(i) - 38
                else:
                    s += ord(i) - 96
                break
    return s


def p2(data):
    data = data.splitlines()
    data = [data[i : i + 3] for i in range(0, len(data), 3)]
    s = 0
    for g1, g2, g3 in data:
        for i in g1:
            if i in g2 and i in g3:
                if i.isupper():
                    s += ord(i) - 38
                else:
                    s += ord(i) - 96
                break
    return s


submit(p1(p.input_data), part="a", day=day, year=year)
submit(p2(p.input_data), part="b", day=day, year=year)
