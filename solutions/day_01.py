"""
1. given array of integers find two that add up to 2020 and return their product
"""
from tools.read_data import read_ints
import numpy as np
from typing import List


def find_sum_in_list(numbers: np.array, goal: int) -> List[int]:
    return list(set(numbers) & set(goal - numbers))


def find_three(numbers: np.array, goal: int) -> int:
    n_sorted = np.sort(numbers)
    other_two_border = n_sorted[0] + n_sorted[1]
    worth_checking = n_sorted[goal - n_sorted >= other_two_border]
    if not worth_checking.size:
        raise Exception("the goal is too small")
    for i in range(worth_checking.size):
        other_two = find_sum_in_list(n_sorted[i+1:], goal - n_sorted[i])
        if other_two:
            return n_sorted[i]*other_two[0]*other_two[1]


if __name__ == "__main__":
    numbers = read_ints("../data/input_0101.txt")
    sum_in_list = find_sum_in_list(numbers, 2020)
    if len(sum_in_list) != 2:
        raise Exception(f"not 2 numbers in the result: {sum_in_list}")
    print(sum_in_list[0] * sum_in_list[1])
    print(find_three(numbers, 2020))
    # test_arr = np.random.randint(1000, 10000, 10**6)
    # print(f"find two test result is {find_sum_in_list(test_arr, 4000)}")
    # print(f"find three test result is {find_three(test_arr, 4000)}")
