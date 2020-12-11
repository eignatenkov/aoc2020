import numpy as np


def line_to_array(line: str) -> np.array:
    result = np.zeros(len(line), dtype=int)
    for i, s in enumerate(line):
        if s == '#':
            result[i] = 1
        elif s == '.':
            result[i] = -1
    return result


def read_input(filename):
    """
    reads the input file, returns a numpy array of ones and zeroes
    :param filename:
    :return:
    """
    one_dim_list = []
    with open(filename) as f:
        for line in f:
            one_dim_list.append(line_to_array(line.strip()))
    return np.vstack(one_dim_list)


def calc_neighbors(board):
    no_floor_board = np.copy(board)
    no_floor_board[no_floor_board < 0] = 0
    neighbors_board = np.zeros(board.shape, dtype=int)
    neighbors_board[:-1, :] += no_floor_board[1:, :]
    neighbors_board[1:, :] += no_floor_board[:-1, :]
    neighbors_board[:, :-1] += no_floor_board[:, 1:]
    neighbors_board[:, 1:] += no_floor_board[:, :-1]
    neighbors_board[1:, 1:] += no_floor_board[:-1, :-1]
    neighbors_board[1:, :-1] += no_floor_board[:-1, 1:]
    neighbors_board[:-1, 1:] += no_floor_board[1:, :-1]
    neighbors_board[:-1, :-1] += no_floor_board[1:, 1:]
    return neighbors_board


def calc_directions(board):
    neighbors_board = np.zeros(board.shape, dtype=int)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            above = board[:i, j]
            if above[above >= 0].size:
                neighbors_board[i, j] += above[above >= 0][-1]
            below = board[i+1:, j]
            if below[below >=0].size:
                neighbors_board[i, j] += below[below >= 0][0]
            left = board[i, :j]
            if left[left >= 0].size:
                neighbors_board[i, j] += left[left >= 0][-1]
            right = board[i, j+1:]
            if right[right >= 0].size:
                neighbors_board[i, j] += right[right >= 0][0]
            bottom_right = np.diagonal(board[i+1:, j+1:])
            if bottom_right[bottom_right >= 0].size:
                neighbors_board[i, j] += bottom_right[bottom_right >= 0][0]
            top_left = np.diagonal(board[:i, :j], offset=j-i)
            if top_left[top_left >= 0].size:
                neighbors_board[i, j] += top_left[top_left >= 0][-1]
            top_right = np.diagonal(board[:i, j+1:][-1::-1])
            if top_right[top_right >= 0].size:
                neighbors_board[i, j] += top_right[top_right >= 0][0]
            bottom_left = np.diagonal(board[i+1:, :j][:, -1::-1])
            if bottom_left[bottom_left >= 0].size:
                neighbors_board[i, j] += bottom_left[bottom_left >= 0][-1]
    return neighbors_board


def update_board(board):
    new_board = np.copy(board)
    neighbors_board = calc_neighbors(board)
    new_board[(board == 0) & (neighbors_board == 0)] = 1
    new_board[(board == 1) & (neighbors_board >= 4)] = 0
    return new_board


def update_board_directions(board):
    new_board = np.copy(board)
    neighbors_board = calc_directions(board)
    print("neighbors")
    print(neighbors_board)
    print()
    new_board[(board == 0) & (neighbors_board == 0)] = 1
    new_board[(board == 1) & (neighbors_board >= 5)] = 0
    return new_board


# next_board = read_input("../data/input_11.txt")
# cur_board = np.zeros(next_board.shape, dtype=int)
# while not np.array_equal(cur_board, next_board):
#     cur_board = np.copy(next_board)
#     next_board = update_board(cur_board)
# print(next_board[next_board > 0].sum())

next_board = read_input("../data/input_11_test.txt")
# print(update_board_directions(next_board))
# print(update_board_directions(update_board_directions(next_board)))
cur_board = np.zeros(next_board.shape, dtype=int)
while not np.array_equal(cur_board, next_board):
    cur_board = np.copy(next_board)
    next_board = update_board_directions(cur_board)
    print(cur_board)
    print()
print(next_board[next_board > 0].sum())
