# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: int(l), input_file.readlines()[0].split(',')))


# %%
def calc_fuel_cost(i: int, data: list[int]):
    cost = 0
    for n in data:
        cost += abs(n - i)

    return cost


def solve_part_1(data: list[int]) -> int:
    cheapest_cost = 99999999

    for i in range(len(data)):
        cost = calc_fuel_cost(i, data)
        if cost < cheapest_cost:
            cheapest_cost = cost

    return cheapest_cost


print(solve_part_1(data))


# %%
def calc_fuel_cost_exp(i: int, data: list[int]):
    cost = 0
    for n in data:
        diff = abs(n - i)
        cost += int((1 + diff) / 2 * diff)

    return cost


def solve_part_2(data: list[int]) -> int:
    cheapest_cost = 99999999

    for i in range(len(data)):
        cost = calc_fuel_cost_exp(i, data)
        if cost < cheapest_cost:
            cheapest_cost = cost

    return cheapest_cost


print(solve_part_2(data))
