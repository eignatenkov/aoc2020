"""
1. given array of integers find two that add up to 2020 and return their product
"""
import numpy as np
from tools.read_data import read_ints


def find_sum_in_list(numbers, goal):
    numbers_sorted = np.sort(numbers)
    diffs = goal - numbers_sorted
    intersection = set(numbers_sorted) & set(diffs)
    return list(intersection)


def find_three(numbers, goal):
    for i in range(numbers.size - 2):
        temp_goal = goal - numbers[i]
        other_two = find_sum_in_list(numbers[i+1:], temp_goal)
        if other_two:
            return numbers[i]*other_two[0]*other_two[1]


if __name__ == "__main__":
    numbers = read_ints("../data/input_0101.txt")
    sum_in_list = find_sum_in_list(numbers, 2020)
    if len(sum_in_list) != 2:
        raise Exception(f"not 2 numbers in the result: {sum_in_list}")
    print(sum_in_list[0] * sum_in_list[1])
    print(find_three(numbers, 2020))
