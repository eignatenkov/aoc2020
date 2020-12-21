def read_input(filename):
    ingredients = set()
    allergens = set()
    i_list = []
    a_list = []
    with open(filename) as f:
        for line in f:
            i, a = line.strip(')\n').split(' (contains ')
            i = i.split(' ')
            a = a.split(', ')
            ingredients |= set(i)
            allergens |= set(a)
            i_list.append(i)
            a_list.append(a)
    return ingredients, allergens, i_list, a_list


ingredients, allergens, i_list, a_list = read_input("../data/input_21.txt")
contains_a = dict()

for a in allergens:
    containing_dishes = [set(i_list[ind]) for ind, d in enumerate(a_list) if a in d]
    contains_a[a] = containing_dishes[0] if len(containing_dishes) == 1 else set.intersection(*containing_dishes)

all_suspicious = set.union(*contains_a.values())
counter = 0
for d in i_list:
    for i in d:
        if i not in all_suspicious:
            counter += 1

print(counter)
for k, v in contains_a.items():
    print(k, v)