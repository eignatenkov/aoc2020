def parse_line(line):
    result = []
    split = line.strip()
    for symb in split:
        if symb != ' ':
            try:
                result.append(int(symb))
            except:
                result.append(symb)
    return result


def find_opening_bracket(line):
    bracket_counter = -1
    for i in range(len(line) - 2, -1, -1):
        symb = line[i]
        if symb == ')':
            bracket_counter -= 1
        elif symb == '(':
            bracket_counter += 1
        if bracket_counter == 0:
            return i


def eval_polish(line, add_prio=False):
    if isinstance(line[-1], int):
        if len(line) == 1:
            return line[0]
        elif line[-2] == '+':
            if not add_prio:
                return line[-1] + eval_polish(line[:-2], add_prio)
            else:
                if isinstance(line[-3], int):
                    return eval_polish(line[:-3] + [line[-3] + line[-1]], add_prio)
                elif line[-3] == ')':
                    obd = find_opening_bracket(line[:-2])
                    return eval_polish(line[:obd] + [eval_polish(line[obd+1:-3], add_prio)] + line[-2:], add_prio)
                else:
                    raise Exception(f"unexpected symbol before +: {line[-3]}")
        elif line[-2] == '*':
            return line[-1] * eval_polish(line[:-2], add_prio)
        else:
            raise Exception(f"Unknown operator {line[-2]}")
    elif line[-1] == ')':
        obd = find_opening_bracket(line)
        if obd == 0:
            return eval_polish(line[1:-1], add_prio)
        return eval_polish(line[:obd] + [eval_polish(line[obd+1:-1], add_prio)], add_prio)
    else:
        raise Exception(f"parsing problem, last element is {line[-1]}")


with open("../data/input_18.txt") as f:
    examples = [parse_line(line) for line in f]
print(sum(eval_polish(e) for e in examples))
print(sum(eval_polish(e, add_prio=True) for e in examples))