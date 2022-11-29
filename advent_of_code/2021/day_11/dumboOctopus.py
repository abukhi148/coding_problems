import numpy as np

with open('input.txt') as f:
    data = [[int(y) for y in x] for x in f.read().split('\n')]
    data = np.matrix(data, dtype=int)
print(data)


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:  # top
        adjacent_indices.append((i - 1, j))
    if i > 0 and j > 0:  # top left
        adjacent_indices.append((i - 1, j - 1))
    if j > 0:  # left
        adjacent_indices.append((i, j - 1))
    if j > 0 and i + 1 < m:  # down left
        adjacent_indices.append((i + 1, j - 1))
    if i + 1 < m:  # down
        adjacent_indices.append((i + 1, j))
    if i + 1 < m and j + 1 < n:  # down right
        adjacent_indices.append((i + 1, j + 1))
    if j + 1 < n:  # right
        adjacent_indices.append((i, j + 1))
    if j + 1 < n and i > 0:
        adjacent_indices.append((i - 1, j + 1))
    return adjacent_indices


m, n = data.shape
flashes = 0
for step in range(2):
    for i in range(m):
        for j in range(n):
            data[i, j] += 1
            if data[i, j] > 9:
                adj = get_adjacent_indices(i, j, m, n)
                for ii, jj in adj:
                    data[ii, jj] += 1

            count = np.count_nonzero(data == 3)

    print(data)
print(flashes)
