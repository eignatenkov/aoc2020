from itertools import chain, combinations
from copy import copy

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def apply_mask(number, mask):
    result = number
    for i, v in enumerate(mask):
        if v != 'X':
            offset = len(mask) - 1 - i
            if v == '1':
                b_mask = 1 << offset
                result = result | b_mask
            else:
                b_mask = ~(1 << offset)
                result = result & b_mask
    return result


def transform_new_mask_to_old_masks(new_mask):
    result = []
    tnm = list(new_mask)
    floating_indices = []
    for i, v in enumerate(new_mask):
        if v == 'X':
            tnm[i] = '0'
            floating_indices.append(i)
        elif v == '0':
            tnm[i] = 'X'
    for subset in powerset(floating_indices):
        next_mask = copy(tnm)
        for ind in subset:
            next_mask[ind] = '1'
        next_mask = ''.join(next_mask)
        result.append(next_mask)
    return result



def apply_mask_to_address(address, mask):
    result = []
    for i, v in enumerate(mask):
        if v == '1':
            offset = len(mask) - 1 - i
            b_mask = 1 << offset
            address = address | b_mask



mem = dict()
cur_mask = ''
with open("../data/input_14.txt") as f:
    for line in f:
        if line.startswith("mask"):
            cur_mask = line.strip()[7:]
        else:
            ind, value = map(int, line.strip()[4:].split('] = '))
            mem[ind] = apply_mask(value, cur_mask)

print(sum(mem.values()))
mem = dict()
cur_mask = ''
with open("../data/input_14.txt") as f:
    for line in f:
        if line.startswith("mask"):
            cur_mask = line.strip()[7:]
            address_masks = transform_new_mask_to_old_masks(cur_mask)
        else:
            ind, value = map(int, line.strip()[4:].split('] = '))
            for am in address_masks:
                m_ind = apply_mask(ind, am)
                mem[m_ind] = value

print(sum(mem.values()))