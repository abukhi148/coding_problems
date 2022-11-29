import itertools


def p1():
    with open("input.txt") as f:
        raw_data = f.read().strip().split("\n")
        data = [line[line.index("|") + 2:].split(" ") for line in raw_data]

    good = [2, 4, 3, 7]

    answer = 0
    for output in data:
        for digit in output:
            if len(digit) in good:
                answer += 1
    print(answer)

# TODO: revise part 2 on a later date. You fucking cunt!
def p2():
    with open("input.txt") as f:
        raw_data = f.read().strip().split("\n")
        data = [[sorted(line[:line.index("|") - 1].split(" ")), line[line.index("|") + 2:].split(" ")] for line in
                raw_data]

    digits_key = ["acedgfb",
                  "cdfbe",
                  "gcdfa",
                  "fbcad",
                  "dab",
                  "cefabd",
                  "cdfgeb",
                  "eafb",
                  "cagedb",
                  "ab"]
    digits = sorted(digits_key)
    digits = tuple(digits)
    answer = 0
    for line in data:
        clues = line[0]
