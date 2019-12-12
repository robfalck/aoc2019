import numpy as np


input_range = '347312-805915'


def contains_repeated_number(sn):
    if '00' in sn or '11' in sn or '22' in sn or '33' in sn or '44' in sn or '55' in sn or '66' in sn or '77' in sn or '88' in sn or '99' in sn:
        return True
    return False

def is_non_decreasing(sn):
    diff = np.diff(np.array([int(s) for s in sn]))
    return np.all(diff >= 0)

def is_valid(n, sn):
    return contains_repeated_number(sn) and is_non_decreasing(sn)

    return False

def part1(low, high):
    valid_numbers = set()
    for n in range(low, high + 1):
        sn = str(n)
        if is_valid(n, sn):
            valid_numbers.add(n)
    print(len(valid_numbers))
    return valid_numbers


if __name__ == '__main__':
    vn = part1(*[int(s) for s in input_range.split('-')])