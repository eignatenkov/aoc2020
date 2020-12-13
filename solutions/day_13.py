import numpy as np
from sympy import mod_inverse

with open("../data/input_13.txt") as f:
    my_ts = int(f.readline())
    raw_schedule = f.readline().strip().split(',')

sch_one = np.array([int(x) for x in raw_schedule if x != 'x'])
time_to_wait = [x - my_ts % x for x in sch_one]
print(min(time_to_wait)*sch_one[time_to_wait.index(min(time_to_wait))])
remainders = np.array([x - raw_schedule.index(str(x)) for x in sch_one])
M = np.prod(sch_one)
M_i = M // sch_one
inverses = [mod_inverse(m, s) for m, s in zip(M_i, sch_one)]
print(np.sum(remainders*M_i*inverses) % M)