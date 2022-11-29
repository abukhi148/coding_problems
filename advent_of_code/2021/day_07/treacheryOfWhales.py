with open('input.txt') as f:
    positions = list(map(int, f.read().split(',')))

def p1():
    optimal_pos = list(set(positions))
    fuel_cost = sum([abs(position - optimal_pos[0]) for position in positions])
    for pos in optimal_pos:
        cost = sum([abs(position - pos) for position in positions])
        fuel_cost = cost if cost < fuel_cost else fuel_cost
    print(fuel_cost)


# TODO: Inefficient AF.Can be improved with dictionaries probably
def p2():
    optimal_pos = [x for x in range(max(positions) + 1)]
    fuel_cost = sum([sum([x for x in range(1, abs(position - optimal_pos[0]) + 1)]) for position in positions])
    for pos in optimal_pos:
        cost = sum([sum([x for x in range(1, abs(position - pos) + 1)]) for position in positions])
        fuel_cost = cost if cost < fuel_cost else fuel_cost
    print(fuel_cost)


p2()
