def parse_input(filename):
    result = dict()
    tests = []
    with open(filename) as f:
        for line in f:
            if ':' in line:
                k, v = line.strip().split(': ')
                if v.startswith("\""):
                    v = [v[1]]
                else:
                    v = [list(map(int, x.split(' '))) for x in v.split(' | ')]
                result[int(k)] = v
            else:
                if line.strip():
                    tests.append(line.strip())
    return result, tests

from itertools import product, chain
def prod_patterns(l_a, l_b):
    return [x[0] + x[1] for x in product(l_a, l_b)]


def is_parsed(val):
    return all(isinstance(x, str) for x in val)


def merge_patterns(l_l_patterns):
    result = []
    for l_p in l_l_patterns:
        result += (prod_patterns(*l_p)) if len(l_p) > 1 else l_p[0]
    return result


def is_input_parsed(rule, rules_dict):
    return all(is_parsed(rules_dict[r]) for r in chain.from_iterable(rule))


def resolve_input(val, rules_dict):
    return [[rules_dict[k] for k in r] for r in val]


rules, tests = parse_input("../data/input_19.txt")
while not is_parsed(rules[0]):
    for k in rules.keys():
        if not is_parsed(rules[k]) and is_input_parsed(rules[k], rules):
            rules[k] = merge_patterns(resolve_input(rules[k], rules))
            break

print(len(set(tests) & set(rules[0])))


def check_test(t, r_x, r_y):
    l = len(r_x[0])
    x_c = 0
    while t[:l] in r_x:
        t = t[l:]
        x_c += 1
    y_c = 0
    while t[:l] in r_y:
        t = t[l:]
        y_c += 1
    if y_c == 0 or x_c <= y_c:
        return False
    if len(t) > 0:
        return False
    return True

print(sum(check_test(t, rules[42], rules[31]) for t in tests))

