# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: [int(i) for i in l.strip('\n')], input_file.readlines()))


#%%
def is_low_point(x: int, y: int, data: list[list[int]]) -> bool:
    adjacents = [
        [x+0, y+1],
        [x+1, y+0],
        [x+0, y-1],
        [x-1, y+0],
    ]

    row_len = len(data[0])
    col_len = len(data)
    val = data[y][x]
    for x2, y2 in adjacents:
        if 0 <= x2 < row_len and 0 <= y2 < col_len and data[y2][x2] <= val:
            return False

    return True


def solve_part_1(data: list[list[int]]) -> int:
    risk_level_sum = 0

    for y, row in enumerate(data):
        for x in range(len(row)):
            if is_low_point(x, y, data):
                risk_level_sum += data[y][x] + 1

    return risk_level_sum


print(solve_part_1(data))
