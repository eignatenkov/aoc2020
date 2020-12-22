def read_input(filename):
    a = []
    b = []
    with open(filename) as f:
        cur_list = a
        for line in f:
            if line.strip() == "Player 2:":
                cur_list = b
            try:
                cur_list.append(int(line.strip()))
            except:
                pass
    return a, b


def play_round(a, b, recursive=False):
    # print(a, b)
    if recursive and a[0] <= len(a) - 1 and b[0] <= len(b) - 1:
        sub_a, sub_b = play_game(a[1:], b[1:], recursive)
        if len(sub_a) == 0:
            return a[1:], b[1:] + [b[0], a[0]]
        else:
            return a[1:] + [a[0], b[0]], b[1:]
    if a[0] > b[0]:
        return a[1:] + [a[0], b[0]], b[1:]
    else:
        return a[1:], b[1:] + [b[0], a[0]]


def play_game(a, b, recursive=False):
    a_states = {tuple(a)}
    while len(a) and len(b):
        a, b = play_round(a, b, recursive)
        if a and tuple(a) in a_states:
            break
        a_states.add(tuple(a))
    return a, b


a, b = read_input("../data/input_22.txt")
usual_a, usual_b = play_game(a, b)


import numpy as np
print((np.array(usual_a) * np.arange(len(usual_a), 0, -1)).sum(), (np.array(usual_b) * np.arange(len(usual_b), 0, -1)).sum())
a, b = read_input("../data/input_22.txt")
rec_a, rec_b = play_game(a, b, recursive=True)
print(rec_a, rec_b)