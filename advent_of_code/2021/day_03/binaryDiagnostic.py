with open('input.txt') as f:
    data = list(map(list, f.read().splitlines()))
    data = [[int(j) for j in i] for i in data]


def data2():
    with open('input.txt') as file:
        return [x.split()[0] for x in file.read().splitlines()]


def p1():
    gamma, epsilon = ('0b', '0b')
    for i in range(len(data[0])):
        zeros = 0
        ones = 0
        for j in range(len(data)):
            if data[j][i] == 0:
                zeros += 1
            else:
                ones += 1
        gamma, epsilon = (gamma + ('1' if ones > zeros else '0'), epsilon + ('1' if ones < zeros else '0'))
    print(int(gamma, 2) * int(epsilon, 2))


def p2():
    # O2 rate
    o2 = data2()
    for i in range(len(o2[0])):
        zeros = 0
        ones = 0
        for j in range(len(o2)):
            if o2[j][i] == '0':
                zeros += 1
            else:
                ones += 1
        common_bit = '1' if ones >= zeros else '0'
        for j in o2[:]:
            if j[i] != common_bit:
                o2.remove(j)
    print(f"Oxygen {int('0b' + o2[0], 2)}")

    # CO2 rate
    co2 = data2()
    for i in range(len(co2[0])):
        zeros = 0
        ones = 0
        for j in range(len(co2[:])):
            if co2[j][i] == '0':
                zeros += 1
            else:
                ones += 1
        common_bit = '1' if ones >= zeros else '0'
        for j in co2[:]:
            if j[i] == common_bit and len(co2) != 1:
                co2.remove(j)
    print(f"Carbon {int('0b' + co2[0], 2)}")

    print(f"Multiply {int('0b' + co2[0], 2) * int('0b' + o2[0], 2)}")

p1()
p2()
