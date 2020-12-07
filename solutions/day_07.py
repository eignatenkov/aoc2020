from collections import defaultdict
from copy import copy


def remove_bag(line):
    if line.endswith(" bags"):
        return line[:-5]
    if line.endswith(" bag"):
        return line[:-4]
    return line


def parse_line(line):
    key, values = line.strip().strip('.').split(" bags contain ")
    values = values.split(', ')
    values = [remove_bag(v).split(' ', maxsplit=1) for v in values]
    return key, values


def create_dict(filename):
    result = dict()
    with open(filename) as f:
        for line in f:
            k, v = parse_line(line)
            result[k] = v
    return result


def create_reversed_dict(filename):
    """
    key - bag
    values - set of bags in which key could be contained
    :param filename:
    :return:
    """
    result = defaultdict(set)
    with open(filename) as f:
        for line in f:
            key, values = parse_line(line)
            for v in values:
                if v[1] != 'other':
                    result[v[1]].add(key)
    return result


def count_bags_containing(reversed_dict, target_bag):
    result = set()
    new_result = reversed_dict[target_bag]
    while result != new_result:
        result = copy(new_result)
        for k in result:
            new_result |= reversed_dict[k]
    return len(new_result)


def count_bags_inside(direct_dict, bag):
    """
    including the top level bag
    :param direct_dict:
    :param bag:
    :return:
    """
    first_level_bags = direct_dict[bag]
    if first_level_bags == [['no', 'other']]:
        return 1
    else:
        return sum(int(flb[0]) * count_bags_inside(direct_dict, flb[1]) for flb in first_level_bags) + 1


if __name__ == "__main__":
    reversed_dict = create_reversed_dict("../data/input_07.txt")
    print(count_bags_containing(reversed_dict, "shiny gold"))
    direct_dict = create_dict("../data/input_07.txt")
    print(count_bags_inside(direct_dict, "shiny gold") - 1)
