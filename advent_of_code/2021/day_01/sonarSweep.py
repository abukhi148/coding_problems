def p1(data=None):
    if data is None:
        with open('input.txt') as f:
            measurements = f.readlines()
            measurements = list(map(int, measurements))
    else:
        measurements = data

    increased = 0
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            increased = increased + 1
    print(increased)


def p2():
    with open('input.txt') as f:
        measurements = f.readlines()
        measurements = [int(x) for x in measurements]
    data = []
    for i in range(2, len(measurements)):
        sum = measurements[i - 2] + measurements[i - 1] + measurements[i]
        data.append(sum)
    p1(data=data)


p1()
p2()
