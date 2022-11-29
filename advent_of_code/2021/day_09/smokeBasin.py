import numpy as np

with open('test.txt') as f:
    data = [[int(y) for y in x] for x in f.read().split("\n")]


def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i - 1, j))
    if i + 1 < m:
        adjacent_indices.append((i + 1, j))
    if j > 0:
        adjacent_indices.append((i, j - 1))
    if j + 1 < n:
        adjacent_indices.append((i, j + 1))
    return adjacent_indices


grid = np.array(data)
m, n = grid.shape


# Part 1
def p1():
    s = 0
    low_points = []
    for i in range(0, m):
        for j in range(0, n):
            adj_idx = get_adjacent_indices(i, j, m, n)
            adj_val = [grid[i, j] for i, j in adj_idx]
            if all(val > grid[i, j] for val in adj_val):
                low_points.append((i, j))
                s += grid[i, j] + 1
    print(low_points)
    print(s)
    return low_points


# Part 2
def p2():
    low_points = p1()
    cur_id = 1
    ids = np.zeros((m, n), dtype=int)
    for i, j in low_points:
        l = [(i, j)]
        visited = set()
        while len(l) > 0:
            i, j = l.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            ids[i, j] = cur_id
            for ii, jj in get_adjacent_indices(i, j, m, n):
                if grid[ii][jj] == 9:
                    continue
                l.append((ii, jj))
        cur_id += 1

    # Find the sizes of biggest basins
    sizes = [0] * cur_id
    for x in ids.flatten():
        sizes[x] += 1
    sizes = sizes[1:]
    sizes.sort()
    print(sizes[-1] * sizes[-2] * sizes[-3])


p1()
p2()
