"""
https://adventofcode.com/2020/day/3
"""
import numpy as np


def line_to_array(line: str) -> np.array:
    result = np.zeros(len(line), dtype=bool)
    for i, s in enumerate(line):
        if s == '#':
            result[i] = True
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


def count_trees(tree_map, x_shift, y_shift):
    counter = 0
    x_cur = 0
    y_cur = 0
    while True:
        x_cur += x_shift
        y_cur = (y_cur + y_shift) % tree_map.shape[1]
        if x_cur >= tree_map.shape[0]:
            break
        counter += tree_map[x_cur, y_cur]
    return counter


if __name__ == "__main__":
    tree_map = read_input("../data/input_03.txt")
    print(count_trees(tree_map, 1, 3))
    product = 1
    for x_slope, y_slope in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
        tree_count = count_trees(tree_map, x_slope, y_slope)
        product *= tree_count
    print(product)
