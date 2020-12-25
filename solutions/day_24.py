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
    return x, y


def count_odd(numbers):
    return sum(n % 2 for n in numbers)


def calc_neighbors(x, y):
    result = []
    for dir in dir_dict:
        x_add, y_add = dir_to_vec(dir)
        result.append((x + x_add, y + y_add))
    return result


def round_tile(x, y, n=5):
    return round(x, n), round(y, n)


def count_black_neighbors(x, y, blacks_rounded):
    result = 0
    for n in calc_neighbors(x, y):
        if round_tile(*n) in blacks_rounded:
            result += 1
    return result


def run_day(blacks):
    all_neighbors = set()
    round_neighbors = set()
    all_neighbors |= blacks
    blacks_rounded = {round_tile(*n) for n in blacks}
    round_neighbors |= blacks_rounded
    for k in blacks:
        neighbors_candidates = set(calc_neighbors(*k))
        for nc in neighbors_candidates:
            rnc = round_tile(*nc)
            if rnc not in round_neighbors:
                round_neighbors.add(rnc)
                all_neighbors.add(nc)
    result = set()
    result_round = set()
    for t in all_neighbors:
        t_round = round_tile(*t)
        n_neighbors = count_black_neighbors(*t, blacks_rounded)
        if t_round not in blacks_rounded and n_neighbors == 2 or t_round in blacks_rounded and 1 <= n_neighbors <= 2:
            if t_round not in result_round:
                result.add(t)
                result_round.add(t_round)
    return result


if __name__ == "__main__":
    tile_list = []
    with open("../data/input_24.txt") as f:
        for line in f:
            tile_list.append(parse_line(line.strip()))

    tile_count = Counter()
    for route in tile_list:
        rp = walk_route(route)
        tile_count[(round(rp[0], 10), round(rp[1], 10))] += 1

    print(count_odd(tile_count.values()))

    blacks = set(k for k, v in tile_count.items() if v % 2)
    for i in range(100):
        blacks = run_day(blacks)
    print(len(blacks))