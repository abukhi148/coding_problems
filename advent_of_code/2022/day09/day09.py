from datetime import date
from aocd import submit
from aocd.models import Puzzle
import numpy as np
from pprint import pprint

day, year = date.today().day, date.today().year
p = Puzzle(day=9, year=year)

# helper functions
def move(v, d):
    if d == "R":
        v += (1, 0)
    elif d == "L":
        v -= (1, 0)
    elif d == "U":
        v += (0, 1)
    else:
        v -= (0, 1)
    return v


def move_diag(h, t):
    for m in [(1, -1), (-1, 1), (1, 1), (-1, -1)]:
        rt = t + m
        if np.linalg.norm(h - rt) <= np.sqrt(2):
            return rt


def parse(data):
    return [(i[0], int(i[1])) for i in (i.split() for i in data.splitlines())]


# TODO: could be simplified
def p1(data):
    h = np.array([0, 0])
    t = np.array([0, 0])
    positions = list()
    for d, s in data:
        for _ in range(s):
            h = move(h, d)
            op = np.linalg.norm(h - t)
            if op == 2:
                t = move(t, d)
            elif op > np.sqrt(2):
                t = move_diag(h, t)
            pos = list(t.copy())
            if pos not in positions:
                positions.append(pos)
    return len(positions)

#TODO: wron movement in point in knot 2
def p2(data):
    positions = list()
    knots = dict()
    for i in range(0, 10):
        knots[i] = np.array([0, 0])
    for d, s in data:
        for _ in range(s):
            knots.update({0: move(knots[0], d)})
            for i in range(1, 10):
                op = np.linalg.norm(knots[i - 1] - knots[i])
                if op == 2:
                    knots.update({i: move(knots[i], d)})
                elif op > np.sqrt(2):
                    knots.update({i: move_diag(knots[i - 1], knots[i])})
                print(i, knots[i])
            print()
            pos = list(knots[9].copy())
            if pos not in positions:
                positions.append(pos)
        pprint(knots)
    return len(positions)


d = """R 5
U 8
L 8
D 3
R 3
"""
data = parse(d)
submit(p1(data), part="a", day=day, year=year)
print(p2(data))
# submit(p2(p.input_data), part="b", day=day, year=year)
