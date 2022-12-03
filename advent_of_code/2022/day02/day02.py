from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)

# TODO simplify p1 into something cleaner
def p1(data):
    d = {"X": ("A", 1), "Y": ("B", 2), "Z": ("C", 3)}
    data = [i.split() for i in data.splitlines()]
    score = 0
    for o, p in data:
        score += d[p][1]
        if d[p][0] == o:
            score += 3
        elif (
            (d[p][0] == "A" and o == "C")
            or (d[p][0] == "C" and o == "B")
            or (d[p][0] == "B" and o == "A")
        ):
            score += 6
    return score


def p2(data):
    moves = {
        "X": ({"A": "C", "C": "B", "B": "A"}, 0),  # lose
        "Y": ({"A": "A", "B": "B", "C": "C"}, 3),  # draw
        "Z": ({"C": "A", "B": "C", "A": "B"}, 6),  # win
    }
    options = {"A": 1, "B": 2, "C": 3}
    score = 0
    data = [i.split() for i in data.splitlines()]
    for o, p in data:
        score += moves[p][1] + options[moves[p][0][o]]
    return score


submit(p1(p.input_data), part="a", day=day, year=year)
submit(p2(p.input_data), part="b", day=day, year=year)
