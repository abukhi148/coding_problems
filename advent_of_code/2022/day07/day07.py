from datetime import date
from aocd import submit
from aocd.models import Puzzle

day, year = date.today().day, date.today().year
p = Puzzle(day=7, year=year)


def parse(data):
    data = [i.split() for i in data.splitlines()]
    data_s = dict()
    for c in data:
        if c[0] == "$":
            if c[1] == "cd" and c[2] != "..":
                curr_dir = c[2]
                data_s[curr_dir] = {"size": 0, "dirs": []}
                ls = False
            else:
                ls = True
        else:
            if ls:
                if c[0] == "dir":
                    data_s[curr_dir]["dirs"].append(c[1])
                else:
                    data_s[curr_dir]["size"] += int(c[0])
    return data_s

#TODO: pending solution 
def p1(data):
    r = list()
    while not all([True if not data[k]["dirs"] else False for k in data]):
        for k, v in data.items():
            if v["dirs"]:
                dir = v["dirs"].pop()
                data[k]["size"] += data[dir]["size"]
    for k, v in data.items():
        if v["size"] <= 100000:
            r.append(v["size"])
    return sum(r)


def p2(data):
    """Solve part 2."""


data = parse(p.input_data)
print(p1(data), sep="\n")
submit(p1(data), part="a", day=7, year=year)
# submit(p2(p.input_data), part="b", day=day, year=year)
