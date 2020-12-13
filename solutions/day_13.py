with open("../data/input_13.txt") as f:
    my_ts = int(f.readline())
    raw_schedule = f.readline().strip().split(',')

print(my_ts)
print(raw_schedule)

sch_one = [int(x) for x in raw_schedule if x != 'x']
print(sch_one)
time_to_wait = [x - my_ts % x for x in sch_one]
print(time_to_wait)
print(min(time_to_wait)*sch_one[time_to_wait.index(min(time_to_wait))])