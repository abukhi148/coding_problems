with open('input.txt') as f:
    data = [chunk for chunk in f.read().strip().split("\n")]
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


def score(line):
    l = []
    for character in line:
        corrupt = False
        for pair in ["()", "[]", "<>", "{}"]:
            if character == pair[0]:
                l.append(character)
                corrupt = True
            elif character == pair[1]:
                if l[-1] == pair[0]:
                    l.pop()
                    corrupt = True
        if not corrupt:
            return scores[character]
    return 0


total_scores = 0
for line in data:
    total_scores += score(line)
print(total_scores)
