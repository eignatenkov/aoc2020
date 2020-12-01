import numpy as np


def read_ints(file_name: str) -> np.array:
    """
    read integer numbers from file_name returns a list of integers
    :param file_name: file name
    :return: np.array of integers
    """
    res = []
    with open(file_name) as f:
        for line in f:
            res.append(int(line))
    return np.array(res, dtype='int')