from datetime import date
from aocd import submit
from aocd.models import Puzzle
import textfsm, operator, math

day, year = date.today().day, date.today().year
p = Puzzle(day=11, year=year)


def op(old, o, n, d=True):
    n = int(n) if n != "old" else old
    if o == "+":
        r = operator.add(old, n)
    elif o == "-":
        r = operator.sub(old, n)
    elif o == "*":
        r = operator.mul(old, n)
    else:
        r = operator.truediv(old, n)
    if d:
        return r // 3
    else:
        return r


def parse(data):
    with open("parser.textfsm") as f:
        data = textfsm.TextFSM(f).ParseTextToDicts(data)
        for i in data:
            for k, v in i.items():
                if k == "st_items":
                    i[k] = list(map(int, v.split(",")))
                elif k == "op":
                    i[k] = v.split()
                else:
                    i[k] = int(v)
            i["inspects"] = 0
    return data


def p1(data):
    for _ in range(20):
        for i in data:
            items = i["st_items"].copy()
            i["st_items"] = list()
            i["inspects"] += len(items)
            for v in items:
                o, n = i["op"]
                r = op(v, o, n)
                if r % i["test"] == 0:
                    data[i["if_true"]]["st_items"].append(r)
                else:
                    data[i["if_false"]]["st_items"].append(r) 
    return math.prod(sorted([i["inspects"] for i in data])[-2:])

#TODO: Modular arithmetic :(
def p2(data, rounds=1):
    for _ in range(rounds):
        for i in data:
            items = i["st_items"].copy()
            i["st_items"] = list()
            i["inspects"] += len(items)
            for v in items:
                o, n = i["op"]
                r = op(v, o, n, d=False)
                if r % i["test"] == 0:
                    data[i["if_true"]]["st_items"].append(r)
                else:
                    data[i["if_false"]]["st_items"].append(r)
            print(i['monkey'], i['inspects'])
        print() 
    return math.prod(sorted([i["inspects"] for i in data])[-2:])


data = parse(p.input_data)
submit(p1(data), part="a", day=11, year=year)
# submit(p2(p.input_data), part="b", day=day, year=year)
