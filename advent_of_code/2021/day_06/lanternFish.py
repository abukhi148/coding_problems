from collections import defaultdict

with open('input.txt') as f:
    population = list(map(int, f.read().split(',')))


def p1():
    days = 80
    for day in range(days):
        for i in range(len(population[:])):
            if population[i] == 0:
                population[i] = 6
                population.append(8)
            else:
                population[i] -= 1
    print(len(population))


def p2():
    frequency = defaultdict(int)
    for i in population:
        frequency[i] += 1
    days = 256
    for day in range(days):
        new_frequency = defaultdict(int)
        for key in frequency:
            if key == 0:
                new_frequency[6] += frequency[key]
                new_frequency[8] = frequency[key]
            else:
                new_frequency[key - 1] += frequency[key]
        frequency = new_frequency
    p = 0
    for key in frequency:
        p += frequency[key]
    print(p)

p2()