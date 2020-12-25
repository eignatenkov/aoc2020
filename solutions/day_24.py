from collections import Counter
DIR_DICT = {'e': 0, 'ne': 1, 'nw': 2, 'w': 3, 'sw': 4, 'se': 5}


def parse_line(line):
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


def dir_to_vec(dir: str):
    """
    neighbors of (0,0) from east counterclockwise:
    (1,0), (0,1), (-1,1), (-1,0), (0,-1), (1,-1)
    """
    x = [1, 0, -1, -1, 0, 1]
    y = [0, 1, 1, 0, -1, -1]
    return x[DIR_DICT[dir]], y[DIR_DICT[dir]]


def walk_route(route):
    x = 0
    y = 0
    for dir in route:
        x_add, y_add = dir_to_vec(dir)
        x += x_add
        y += y_add
    return x, y


def calc_neighbors(x, y):
    result = []
    for dir in DIR_DICT:
        x_add, y_add = dir_to_vec(dir)
        result.append((x + x_add, y + y_add))
    return result


def run_day(blacks):
    all_neighbors = set.union(blacks, *(calc_neighbors(*k) for k in blacks))
    result = set()
    for t in all_neighbors:
        n_neighbors = sum(1 for n in calc_neighbors(*t) if n in blacks)
        if t not in blacks and n_neighbors == 2 or t in blacks and 1 <= n_neighbors <= 2:
            result.add(t)
    return result


if __name__ == "__main__":
    tile_list = []
    with open("../data/input_24.txt") as f:
        for line in f:
            tile_list.append(parse_line(line.strip()))

    tile_count = Counter()
    for route in tile_list:
        tile_count[walk_route(route)] += 1
    print(sum(n % 2 for n in tile_count.values()))

    blacks = set(k for k, v in tile_count.items() if v % 2)
    for i in range(100):
        blacks = run_day(blacks)
    print(len(blacks))
