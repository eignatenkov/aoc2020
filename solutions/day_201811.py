import numpy as np
from tqdm import trange

def power_level(x, y, gsn):
    rack_id = x + 10
    pl = (rack_id * y + gsn) * rack_id
    return pl // 100 % 10 - 5


if __name__ == "__main__":
    power_grid = np.zeros((300, 300), dtype=int)
    gsn = 694
    for i in range(300):
        for j in range(300):
            power_grid[i, j] = power_level(i + 1, j + 1, gsn)
    max_sum = -1000
    max_i = 0
    max_j = 0
    max_size = 0
    for size in trange(1, 301):
        for i in range(301 - size):
            for j in range(301 - size):
                square_sum = power_grid[i:i+size, j:j+size].sum()
                if square_sum > max_sum:
                    max_sum = square_sum
                    max_i = i+1
                    max_j = j + 1
                    max_size = size
    print(max_i, max_j, max_size, max_sum)
