from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


options = [38,76,4,61,37,19,2,3,5,18,23]

letters_dict = {
    1: 38,
    2: 76,
    3: 4,
    4: 61,
    5: 37,
    6: 19,
    7: 2,
    8: 3,
    9: 5,
    10: 18,
    11: 23
}

for subset in powerset(letters_dict.keys()):
    n_letters = sum(letters_dict[k] for k in subset)
    if n_letters == 143 and 1 in subset:
        print(sorted(subset), sorted(set(range(1, 12)) - set(subset)))

from math import sqrt
def glue_per_cube(k):
    area = 625*(1 + 1/k**2 + 1/(k+1)**2)
    side = sqrt(area)
    perimeter = 4 * side
    glue = perimeter * 0.15
    return glue

total_glue = 0

for i in range(1, 200):
    total_glue += glue_per_cube(i)
    if total_glue > 2020:
        print(total_glue, glue_per_cube(i), i)
        break