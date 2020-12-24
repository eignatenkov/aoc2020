from math import sin, cos, pi
from collections import Counter


def parse_line(line):
    """
    seseesenweseseseswnwnwseswneswsesenwse to list of commands
    :param line:
    :return:
    """
    result = []
    cur_i = 0
    while cur_i < len(line):
        if line[cur_i] in {'e', 'w'}:
            result.append(line[cur_i])
            cur_i += 1
        else:
            result.append(line[cur_i:cur_i+2])
            cur_i += 2
    return result


dir_dict = {
    'e': 0,
    'ne': 1,
    'nw': 2,
    'w': 3,
    'sw': 4,
    'se': 5
}


def dir_to_vec(dir: str):
    angle = pi/3*dir_dict[dir]
    return cos(angle), sin(angle)


def walk_route(route):
    x = 0
    y = 0
    for dir in route:
        x_add, y_add = dir_to_vec(dir)
        x+= x_add
        y += y_add
    return round(x, 5), round(y, 5)


def count_odd(numbers):
    return sum(n % 2 for n in numbers)


if __name__ == "__main__":
    tile_list = []
    with open("../data/input_24.txt") as f:
        for line in f:
            tile_list.append(parse_line(line.strip()))

    tile_count = Counter()
    for route in tile_list:
        tile_count[walk_route(route)] += 1

    print(count_odd(tile_count.values()))