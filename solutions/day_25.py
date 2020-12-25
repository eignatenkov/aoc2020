"""
input
10604480
4126658
"""


def transform(inp, loop_size):
    result = 1
    for i in range(loop_size):
        result = result * inp % 20201227
    return result


def find_loop_size(inp, output):
    result = 1
    loop_size = 0
    while result != output:
        result = result * inp % 20201227
        loop_size += 1
    return loop_size


print(transform(7, 8))
print(find_loop_size(7, 17807724))

cpk = 10604480
dpk = 4126658
cls = find_loop_size(7, cpk)
dls = find_loop_size(7, dpk)
print(transform(cpk, dls))
print(transform(dpk, cls))