with open('input.txt') as f:
    movements = [x.split() for x in f.readlines()]
    movements = [(x[0], int(x[1])) for x in movements]


# Part 1
def p1():
    depth = 0
    position = 0
    for action, distance in movements:
        if action == 'up':
            depth = depth - distance
        elif action == 'down':
            depth = depth + distance
        elif action == 'forward':
            position = position + distance
    print(f'Part 1 --> depth: {depth}, distance: {position}')
    print(f'Multiplication {depth * position}')


# Part 2
def p2():
    aim = 0
    position = 0
    depth = 0
    for action, distance in movements:
        if action == 'up':
            aim -= distance
        elif action == 'down':
            aim += distance
        elif action == 'forward':
            position += distance
            depth += aim * distance
    print(f'depth: {depth}, position: {position}')
    print(f'Multiplication {depth * position}')


p1()
p2()
