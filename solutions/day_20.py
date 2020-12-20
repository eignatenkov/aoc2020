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


def align_to_above(border, tile):
    for k in range(4):
        new_tile = np.rot90(tile, k)
        if np.array_equal(new_tile[0, :],border):
            return new_tile
        new_tile = np.flipud(new_tile)
        if np.array_equal(new_tile[0, :],border):
            return new_tile
    raise Exception(f"tile {tile} didn't match to border{border}")


def align_top_left(tiles, match_dict):
    for k, v in match_dict.items():
        if len(v) == 2:
            break

    n_a, n_b = (tiles[i] for i in v)
    for a in range(4):
        rotated = np.rot90(tiles[k], a)
        for top_left in (rotated, np.flipud(rotated)):
            try:
                a_a = align_to_left(top_left[:, -1], n_a)
                a_b = align_to_above(top_left[-1, :], n_b)
                return k, top_left
            except:
                try:
                    a_a = align_to_left(top_left[:, -1], n_b)
                    a_b = align_to_above(top_left[-1, :], n_a)
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
                match_dict[cur_index].remove(n)
                break
            except:
                continue
    # finding the leftmost for the next row
    next_left = None
    for n in match_dict[k]:
        try:
            next_left = align_to_above(top_left[-1, :], tiles[n])
            break
        except:
            continue
    return full_pic, match_dict, n, next_left


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

k, top_left = align_top_left(tiles, match_dict)
curr_pic, match_dict, n, next_left = make_row(tiles, match_dict, k, top_left)
full_pic = curr_pic
while True:
    try:
        curr_pic, match_dict, n, next_left = make_row(tiles, match_dict, n, next_left)
        full_pic = np.vstack((full_pic, curr_pic))
    except:
        break


def check_pattern(pic, i, j):
    return pic[i, j + 18] and pic[i + 1, j] and pic[i + 1, j + 5] and pic[i + 1, j + 6] and \
           pic[i + 1, j + 11] and pic[i + 1, j + 12] and pic[i + 1, j + 17] and \
           pic[i + 1, j + 18] and pic[i + 1, j + 19] and pic[i + 1, j + 17] and \
           pic[i + 2, j + 1] and pic[i + 2, j + 4] and pic[i + 2, j + 7] and pic[i + 2, j + 10] and \
           pic[i + 2, j + 13] and pic[i + 2, j + 16]


def count_monsters(pic):
    c = 0
    for i in range(pic.shape[0] - 2):
        for j in range(pic.shape[1] - 19):
            c += check_pattern(pic, i, j)
    return c


for a in range(4):
    rotated = np.rot90(full_pic, a)
    for fp in (rotated, np.flipud(rotated)):
        print(count_monsters(fp))

print(full_pic.sum() - 29*15)