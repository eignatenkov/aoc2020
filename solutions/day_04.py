import re


def parse_passport_data(text):
    k_v_pairs = text.split()
    return {item.split(':')[0]:item.split(':')[1] for item in k_v_pairs}


def is_number(string, lower, higher):
    try:
        n = int(string)
        return lower <= n <= higher
    except:
        return False


def check_height(string):
    if string.endswith('cm'):
        return is_number(string[:-2], 150, 193)
    if string.endswith('in'):
        return is_number(string[:-2], 59, 76)
    return False


def is_passport_valid(passport, strict=False):
    """
    The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID) - optional
    """
    keys_to_check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    if not strict:
        return keys_to_check.issubset(set(passport.keys()))
    checks = [is_number(passport['byr'], 1920, 2002), is_number(passport['iyr'], 2010, 2020),
              is_number(passport['eyr'], 2020, 2030),
              passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
              re.match("^[0-9]{9}$", passport['pid']) is not None,
              re.match("^#[a-f0-9]{6}$", passport['hcl']) is not None,
              check_height(passport['hgt'])]
    return sum(checks) == 7


def read_input(filename):
    result = []
    cur_pass_text = ''
    with open(filename) as f:
        for line in f:
            if line == '\n':
                result.append(parse_passport_data(cur_pass_text))
                cur_pass_text = ''
            else:
                cur_pass_text += line
        result.append(parse_passport_data(cur_pass_text))
    return result


if __name__ == "__main__":
    passports = read_input("../data/input_04.txt")
    print(len(passports))
    valid_passports = [p for p in passports if is_passport_valid(p)]
    print(len(valid_passports))
    strictly_valid_passports = [p for p in valid_passports if is_passport_valid(p, strict=True)]
    print(len(strictly_valid_passports))
