from tqdm import trange


def init_dict(numbers):
    result = dict()
    for i, n in enumerate(numbers):
        result[n] = i + 1
    return result

input = [1,0,16,5,17,4]

memory = init_dict(input[:-1])

last_number = input[-1]

for i in trange(len(input), 30000000):
    if last_number in memory:
        next_number = i - memory[last_number]
        memory[last_number] = i
        last_number = next_number
    else:
        memory[last_number] = i
        last_number = 0

print(last_number)
