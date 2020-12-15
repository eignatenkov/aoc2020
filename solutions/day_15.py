def init_dict(numbers):
    result = dict()
    for i, n in enumerate(numbers):
        result[n] = i + 1

memory = init_dict()
