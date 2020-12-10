from tools.read_data import read_ints
import numpy as np


ints = read_ints("../data/input_09.txt")
for i, n in enumerate(ints[25:]):
    prevs = ints[i:i+25]
    diffs = n - prevs
    if not set(prevs) & set(diffs):
        print(n)
        bad_number = n
        break


for i in range(ints.size - 1):
    cumsums = np.cumsum(ints[i:])
    if bad_number in cumsums and bad_number != cumsums[0]:
        cs_l = list(cumsums)
        last_index = cs_l.index(bad_number)
        c_range = ints[i:(i+last_index + 1)]
        print(c_range.min(), c_range.max(), c_range.min() + c_range.max())