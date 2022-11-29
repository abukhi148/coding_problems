import numpy as np

with open('input.txt') as f:
    data = [x.rsplit() for x in f.readlines()]
    draws = [int(x) for x in data.pop(0)[0].split(',')]
    data = [[[int(y), 0] for y in x] for x in data if x != []]
    boards = np.array_split(data, len(data) / 5)


def detect_win(board):
    for row in range(5):
        if all([board[row][i][1] for i in range(5)]):
            return True
    for col in range(5):
        if all([board[i][col][1] for i in range(5)]):
            return True
    return False


def get_points(board):
    s = 0
    for col in range(5):
        for row in range(5):
            if board[col][row][1] != 1:
                s += board[col][row][0]
    return s


def p1():
    for draw in draws:
        for board in boards:
            for col in range(5):
                for row in range(5):
                    if board[col][row][0] == draw:
                        board[col][row][1] = 1
                        if detect_win(board):
                            return get_points(board) * draw


def p2():
    win_b = []
    for draw in draws:
        for i in range(len(boards)):
            for col in range(5):
                for row in range(5):
                    if boards[i][col][row][0] == draw:
                        boards[i][col][row][1] = 1
                        if detect_win(boards[i]):
                            if i not in win_b:
                                win_b.append(i)
                                if len(win_b) == len(boards):
                                    return get_points(boards[i]) * draw

print(p1())
print(p2())
