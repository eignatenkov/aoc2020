from copy import copy


def read_input(filename):
    result = []
    with open(filename) as f:
        for line in f:
            command, number_str = line.strip().split(' ')
            result.append((command, int(number_str)))
    return result


def find_loop(commands, acc_value=0):
    visited = [False] * len(commands)
    cur_index = 0
    while True:
        if cur_index >= len(commands):
            return 'done', acc_value
        cur_command, cur_value = commands[cur_index]
        if visited[cur_index]:
            return 'loop', acc_value
        visited[cur_index] = True
        if cur_command == 'jmp':
            cur_index += cur_value
        else:
            cur_index += 1
            if cur_command == "acc":
                acc_value += cur_value


def change_to_work(commands):
    for i in range(len(commands)):
        if commands[i][0] in {'jmp', 'nop'}:
            test_commands = copy(commands)
            test_commands[i] = ('nop', commands[i][1]) if commands[i][0] == 'jmp' else ('jmp', commands[i][1])
            run_results = find_loop(test_commands)
            if run_results[0] == 'done':
                return run_results[1]


if __name__ == "__main__":
    commands = read_input("../data/input_08.txt")
    print(find_loop(commands))
    print(change_to_work(commands))
