def code_to_int(code):
    row = code[:7]
    column = code[7:]
    row_int = int(''.join(['1' if s == 'B' else '0' for s in row]), 2)
    column_int = int(''.join(['1' if s == 'R' else '0' for s in column]), 2)
    return row_int * 8 + column_int


def read_input(filename):
    result = list()
    with open(filename) as f:
        for line in f:
            result.append(line.strip())
    return result


if __name__ == "__main__":
    boarding_passes = read_input("../data/input_05.txt")
    seat_ids = [code_to_int(bp) for bp in boarding_passes]
    print(max(seat_ids))
    seat_ids_sorted = sorted(seat_ids)
    for prev_seat, cur_seat in zip(seat_ids_sorted[:-1], seat_ids_sorted[1:]):
        if prev_seat + 1 != cur_seat:
            print(prev_seat + 1)
