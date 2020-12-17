import numpy as np
from tqdm import trange

grid = np.zeros((25,25,15,15), dtype=bool)

offset = 7

with open("../data/input_17.txt") as f:
    for i, line in enumerate(f):
        for j, symb in enumerate(line.strip()):
            if symb == '#':
                grid[offset + i, offset + j, offset, offset] = 1


def update_grid(grid):
    new_grid = np.zeros(grid.shape, dtype=bool)
    for i in range(1, grid.shape[0] - 1):
        for j in range(1, grid.shape[1] - 1):
            for k in range(1, grid.shape[2] - 1):
                for l in range(1, grid.shape[3] - 1):
                    neighbors = grid[i-1:i+2, j-1:j+2, k-1:k+2, l-1:l+2].sum() - grid[i,j,k, l]
                    if grid[i,j,k,l] and neighbors in [2,3]:
                        new_grid[i,j,k,l] = True
                    elif not grid[i,j,k,l] and neighbors == 3:
                        new_grid[i,j,k,l] = True
    return new_grid


for i in range(6):
    grid = update_grid(grid)

print(grid.sum())