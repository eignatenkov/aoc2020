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
        result += (prod_patterns(*l_p))
    return result


def is_input_parsed(rule, rules_dict):
    return all(is_parsed(rules_dict[r]) for r in chain.from_iterable(rule))


def resolve_input(val, rules_dict):
    return [[rules_dict[k] for k in r] for r in val]


rules, tests = parse_input("../data/input_19.txt")
print(rules)

while not is_parsed(rules[0]):
    for k in rules.keys():
        if not is_parsed(rules[k]) and is_input_parsed(rules[k], rules):
            print(rules[k])
            rules[k] = merge_patterns(resolve_input(rules[k], rules))
            print(k, rules[k])
            break

print(rules[0])
