from aocd import submit
from aocd.models import Puzzle

p = Puzzle(day=1, year=2022)


def p1(data):
    return max([sum(map(int, i.split())) for i in data.split("\n\n")])


def p2(data):
    arr = sorted([sum(map(int, i.split())) for i in data.split("\n\n")])
    return sum(arr[-3:])


#submit(p1(p.input_data), part="a", day=1, year=2022)
#submit(p2(p.input_data), part="b", day=1, year=2022)
print(p.title)