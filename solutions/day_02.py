"""
https://adventofcode.com/2020/day/2
"""
from collections import namedtuple

Entry = namedtuple("Entry", ['min', 'max', 'letter', 'pwd'])


def read_input(filename):
    """
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    min-max amount of appearances of a letter: password
    :param filename:
    :return:
    """
    entries = []
    with open(filename) as f:
        for line in f:
            minmax, letter, pwd = line.strip().split(' ')
            letter = letter.strip(':')
            min_ap, max_ap = map(int, minmax.split('-'))
            entries.append(Entry(min_ap, max_ap, letter, pwd))
    return entries


def validate_entry(entry: Entry) -> bool:
    return entry.min <= sum(1 for l in entry.pwd if l == entry.letter) <= entry.max


def validate_entry_new(entry: Entry) -> bool:
    return ((entry.pwd[entry.min - 1] == entry.letter) + (entry.pwd[entry.max - 1] == entry.letter)) == 1


if __name__ == "__main__":
    entries = read_input("../data/input_0201.txt")
    print(sum(validate_entry(entry) for entry in entries))
    print(sum(validate_entry_new(entry) for entry in entries))