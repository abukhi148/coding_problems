from datetime import date
from aocd import submit
from aocd.models import Puzzle
import numpy as np
from pprint import pprint

day, year = date.today().day, date.today().year
p = Puzzle(day=8, year=year)


def parse(data):
    grid = np.array([list(map(int, list(i))) for i in data.split()])
    return grid


def p1(data):
    rows, cols = data.shape
    visible = data.size
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            t, b = data[:i, j], data[i + 1 :, j]
            l, r = data[i, :j], data[i, j + 1 :]
            if not any([all(data[i, j] > x for x in side) for side in (t, b, r, l)]):
                visible -= 1
    return visible

#TODO: too slow -> optimize solutions 44s
def p2(data):
    scores = list()
    rows, cols = data.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            t, b = data[:i, j][::-1], data[i + 1 :, j]
            l, r = data[i, :j][::-1], data[i, j + 1 :]
            score = list()
            for side in (t, l, r, b):
                s = 0
                for x in side:
                    s += 1
                    if data[i, j] <= x:
                        break
                score.append(s)
            scores.append(np.prod(score))
    return max(scores)


data = parse(p.input_data)
submit(p1(p.input_data), part="a", day=day, year=year)
submit(p2(data), part="b", day=day, year=year)
