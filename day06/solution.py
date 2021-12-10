# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: int(l), input_file.readlines()[0].split(',')))

# %%
def sim_fish(fish: int, day_count: int) -> int:
    fish_count = 1

    while day_count > 0:
        fish -= 1
        if fish < 0:
            fish = 6
            fish_count += sim_fish(8, day_count-1)

        day_count -= 1

    return fish_count


def solve_part_1(data: list, day_count: int) -> int:
    fish_count = 0

    for fish in data:
        fish_count += sim_fish(fish, day_count)

    return fish_count


print(solve_part_1(data, 80))

# %%
def sim_fish_memo(fish: int, day_count: int, memo: dict) -> int:
    memo_key = str(fish) + ':' + str(day_count)
    if memo_key in memo:
        return memo[memo_key]

    fish_count = 1

    while day_count > 0:
        fish -= 1
        if fish < 0:
            fish = 6
            fish_count += sim_fish_memo(8, day_count-1, memo)

        day_count -= 1

    memo[memo_key] = fish_count
    return fish_count


def solve_part_2(data: list, day_count: int) -> int:
    memo = {}
    fishCount = 0

    for fish in data:
        fishCount += sim_fish_memo(fish, day_count, memo)

    return fishCount


print(solve_part_2(data, 256))
