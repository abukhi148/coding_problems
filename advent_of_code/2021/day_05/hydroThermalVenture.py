import numpy as np

with open('input.txt') as f:
    data = [x.strip().split(' -> ') for x in f.readlines()]
    data = [[tuple(map(int, j.split(','))) for j in i] for i in data]

highest = 0
for i in data:
    for x, y in i:
        if x >= highest:
            highest = x
        if y >= highest:
            highest = y
grid = np.zeros((highest + 1, highest + 1), dtype=int)
for i in data:
    x0, y0 = i[0]
    x1, y1 = i[1]
    v = (x1 - x0, y1 - y0)

    # vertical movement
    if x0 == x1:
        if y1 >= y0:
            for row in range(y0, y1 + 1):
                grid[row][x0] += 1
        else:
            for row in range(y1, y0 + 1):
                grid[row][x0] += 1
    # horizontal movement
    elif y0 == y1:
        if x1 >= x0:
            for col in range(x0, x1 + 1):
                grid[y0][col] += 1
        else:
            for col in range(x1, x0 + 1):
                grid[y0][col] += 1
    # diagonal movement
    else:
        for i in range(abs(v[0]) + 1):
            # top right
            if v[0] > 0 and v[1] > 0:
                grid[y0 + i][x0 + i] += 1
            # top left
            elif (v[0] < 0) and (v[1] > 0):
                grid[y0 + i][x0 - i] += 1
            # bottom left
            elif v[0] < 0 and v[1] < 0:
                grid[y0 - i][x0 - i] += 1
            # bottom right
            elif (v[0] > 0) and (v[1] < 0):
                grid[y0 - i][x0 + i] += 1
print((grid > 1).sum())
