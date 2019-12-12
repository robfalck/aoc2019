import numpy as np
import re

input_range = '347312-805915'

def contains_repeated_number(n):
    sn = str(n)
    for i in range(10):
        remainder = re.sub(fr'{i}{i}{i}+','.', sn)
        if f'{i}{i}' in remainder:
            return True
    return False

def is_non_decreasing(n):
    sn = str(n)
    diff = np.diff(np.array([int(s) for s in sn]))
    return np.all(diff >= 0)

def part2(low, high):
    non_decreasing =  [num for num in range(low, high + 1) if is_non_decreasing(num)]
    valid = set([num for num in non_decreasing if contains_repeated_number(num)])
    return valid

if __name__ == '__main__':
    vn = part2(*[int(s) for s in input_range.split('-')])

    print(len(vn))
