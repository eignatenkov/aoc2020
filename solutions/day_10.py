from tools.read_data import read_ints
import numpy as np
import pandas as pd

adapters = read_ints("../data/input_10.txt")

adapters = np.sort(adapters)
adapters = np.append(adapters, adapters[-1] + 3)
adapters = np.insert(adapters, 0, 0)
diffs = pd.Series(adapters[1:] - adapters[:-1])
print(diffs.values)
print(diffs.value_counts())
print(4*2*4*7*4*7*2*7*4*7*4*4*4*4*7*7*7*4*4)