import numpy as np
from collections import defaultdict


def read_input(filename):
    result = dict()
    with open(filename) as f:
        cur_name = ''
        cur_array = np.zeros((10,10), dtype=int)
        row_index = 0
        for line in f:
            if not line.strip():
                result[cur_name] = cur_array
                cur_name = ''
                cur_array = np.zeros((10,10), dtype=int)
                row_index = 0
            elif line.startswith("Tile"):
                cur_name = int(line.strip()[5:-1])
            else:
                for i, symb in enumerate(line.strip()):
                    if symb == '#':
                        cur_array[row_index, i] = 1
                row_index += 1
        result[cur_name] = cur_array
    return result


def get_borders(tile):
    return {tuple(a) for a in [tile[0, :], tile[0, ::-1], tile[-1, :], tile[-1, ::-1], tile[:, 0], tile[::-1, 0], tile[:, -1], tile[::-1, -1]]}


def check_match(tile_a, tile_b):
    return len(get_borders(tile_a) & get_borders(tile_b)) > 0


def align_to_left(border, tile):
    for k in range(4):
        new_tile = np.rot90(tile, k)
        if np.array_equal(new_tile[:, 0],border):
            return new_tile
        new_tile = np.flipud(new_tile)
        if np.array_equal(new_tile[:, 0],border):
            return new_tile
    raise Exception(f"tile {tile} didn't match to border{border}")


def align_top_left(tiles, match_dict):
    for k, v in match_dict.items():
        if len(v) == 2:
            break
    print(k, v)
    for a in range(4):
        top_left = np.rot90(tiles[k], a)
        for n in v:
            try:
                n_t = align_to_left(top_left[:, -1], tiles[n])
                return k, top_left
            except:
                continue


def make_row(tiles, match_dict, k, top_left):
    full_pic = top_left[1:-1, 1:-1]
    cur_right = top_left
    cur_index = k
    found = True
    while found:
        cur_border = cur_right[:, -1]
        neighbors = match_dict[cur_index]
        found = False
        for n in neighbors:
            try:
                cur_right = align_to_left(cur_border, tiles[n])
                cur_index = n
                full_pic = np.hstack((full_pic, cur_right[1:-1, 1:-1]))
                found = True
                break
            except:
                continue


tiles = read_input("../data/input_20.txt")
print(len(tiles))
match_dict = defaultdict(list)
for i, tile_a in tiles.items():
    for j, tile_b in tiles.items():
        if check_match(tile_a, tile_b) and i != j:
            match_dict[i].append(j)

prod = 1
for k, v in match_dict.items():
    if len(v) == 2:
        prod *=k
print(prod)

print(align_top_left(tiles, match_dict))
