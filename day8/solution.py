# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: (l.split(' | ')[0].split(' '), l.split(' | ')[1].strip('\n').split(' ')), input_file.readlines()))


# %%
def solve_part_1(data: list[(str, str)]) -> int:
    known_digit_lengths = [2, 4, 3, 7] # digits: 1, 4, 7, 8
    known_digit_count = 0

    for (signals, digits) in data:
        for digit in digits:
            if len(digit) in known_digit_lengths:
                known_digit_count += 1

    return known_digit_count


print(solve_part_1(data))


# %%
def solve_part_2(data: list[(str, str)]) -> int:
    pass


print(solve_part_2(data))