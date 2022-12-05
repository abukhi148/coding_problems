from datetime import date
from aocd import submit
from aocd.models import Puzzle
from parse import parse
from collections import defaultdict

day, year = date.today().day, date.today().year
p = Puzzle(day=day, year=year)


def parse_data(data):
    data = data.splitlines()
    crates, moves = data[: data.index("")], data[data.index("") + 1 :]
    crates.pop().split()
    stacks = defaultdict(list)
    for crate in reversed(crates):
        for i, letter in enumerate(crate[1::4]):
            if letter != " ":
                stacks[i + 1].append(letter)
    r_moves = list()
    for move in moves:
        r = parse("move {amount:d} from {from:d} to {to:d}", move)
        r_moves.append(r.named)
    return stacks, r_moves


# TODO: solution is slow AF, think of ways to optimize it -> 44s OMG
def p1(stacks, moves):
    for move in moves:
        for _ in range(move["amount"]):
            stacks[move["to"]].append(stacks[move["from"]].pop())
    return "".join([v.pop() for v in stacks.values()])


# TODO: no good this is even worse -> 55s
def p2(stacks, moves):
    for move in moves:
        stacks[move["to"]] += stacks[move["from"]][-move["amount"] :]
        del stacks[move["from"]][-move["amount"] :]
    return "".join([v.pop() for v in stacks.values()])


s, m = parse_data(p.input_data)
submit(p1(s, m), part="a", day=day, year=year)
submit(p2(s, m), part="b", day=day, year=year)
