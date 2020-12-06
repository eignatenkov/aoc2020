def read_input_sets(filename):
    result = []
    cur_group = []
    with open(filename) as f:
        for line in f:
            if line == '\n':
                result.append(cur_group)
                cur_group = []
            else:
                cur_group.append(set(line.strip()))
        result.append(cur_group)
    return result


if __name__ == "__main__":
    per_group_sets = read_input_sets("../data/input_06.txt")
    per_group_union_sizes = [len(set.union(*s)) for s in per_group_sets]
    per_group_intersection_sizes = [len(set.intersection(*s)) for s in per_group_sets]
    print(sum(per_group_union_sizes))
    print(sum(per_group_intersection_sizes))
