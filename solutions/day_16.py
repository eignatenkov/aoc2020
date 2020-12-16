def read_input(filename):
    rules = dict()
    your_ticket = []
    nearby_tickets = []
    with open(filename) as f:
        cur_line = f.readline()
        while cur_line != '\n':
            k, v = cur_line.split(': ')
            v = v.strip().split(' or ')
            rules[k] = [tuple(map(int, x.split('-'))) for x in v]
            cur_line = f.readline()
        cur_line = f.readline()
        cur_line = f.readline()
        your_ticket = list(map(int, cur_line.strip().split(',')))
        cur_line = f.readline()
        cur_line = f.readline()
        cur_line = f.readline()
        while cur_line:
            # print(cur_line)
            nearby_tickets.append(list(map(int, cur_line.strip().split(','))))
            cur_line = f.readline()

    return rules, your_ticket, nearby_tickets


def is_invalid(v, r):
    return v < r[0][0] or v > r[1][1] or (r[0][1] < v < r[1][0])


def check_ticket(ticket, rules):
    for v in ticket:
        if all([is_invalid(v, r) for r in rules.values()]):
            return v


def is_rule_valid(rule, values):
    return not any(is_invalid(v, rule) for v in values)

from collections import defaultdict
def find_map(tickets, rules):
    options = defaultdict(list)
    for name, rule in rules.items():
        for i in range(len(tickets[0])):
            values_to_check = [t[i] for t in tickets]
            if is_rule_valid(rule, values_to_check):
                options[name].append(i)

    result = dict()
    while options:
        remove_value = -1
        for k, v in options.items():
            if len(v) == 1:
                result[k] = v[0]
                options.pop(k)
                remove_value = v[0]
                break
        for k in options.keys():
            try:
                options[k].remove(remove_value)
            except:
                pass
    return result


rules, your_ticket, nearby_tickets = read_input("../data/input_16.txt")
invalid_checks = [check_ticket(t, rules) for t in nearby_tickets]
invalids = [i for i in invalid_checks if i]
valid_tickets = [nearby_tickets[i] for i, ic in enumerate(invalid_checks) if ic is None]
print(sum(invalids))
field_map = find_map(valid_tickets, rules)
prod = 1
for f_name, index in field_map.items():
    if f_name.startswith('departure'):
        prod *= your_ticket[index]
print(prod)
