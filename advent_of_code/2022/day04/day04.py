from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)


def parse(data):
    data = [i.split(",") for i in data.splitlines()]
    data = [
        (tuple(map(int, j.split("-"))), tuple(map(int, k.split("-")))) for j, k in data
    ]
    return data


def p1(data):
    s = 0
    for i, j in data:
        if all((i[0] <= j[0], i[1] >= j[1])) or all((i[0] >= j[0], i[1] <= j[1])):
            s += 1
    return s


# TODO try to simplify, without the use of 2 for loops
def p2(data):
    s = 0
    for i, j in data:
        pair1 = list(range(i[0], i[1] + 1))
        pair2 = list(range(j[0], j[1] + 1))
        for x in pair1:
            if x in pair2:
                s += 1
                break
    return s


p_input = parse(p.input_data)
submit(p1(p_input), part="a", day=day, year=year)
submit(p2(p_input), part="b", day=day, year=year)