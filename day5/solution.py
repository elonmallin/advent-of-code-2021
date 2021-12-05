# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

def transform_line(l):
    (x1, y1, x2, y2) = re.findall('(\d+),(\d+) -> (\d+),(\d+)', l)[0]

    return ((int(x1), int(y1)), (int(x2), int(y2)))


data = list(map(transform_line, input_file.readlines()))


def vector_magnitude(v):
    return math.sqrt(v[0]*v[0] + v[1]*v[1])


def vector_normalize(v):
    m = vector_magnitude(v)

    return (v[0]/m, v[1]/m)


def get_step_vector(start, end):
    v = (end[0] - start[0], end[1] - start[1])
    v = vector_normalize(v)

    if v[0] > 0:
        v = (math.ceil(v[0]), v[1])
    if v[0] < 0:
        v = (math.floor(v[0]), v[1])
    if v[1] > 0:
        v = (v[0], math.ceil(v[1]))
    if v[1] < 0:
        v = (v[0], math.floor(v[1]))

    return v


def get_points(start, end):
    points = [end]

    direction = get_step_vector(start, end)
    step = start
    while step != end:
        points.append(step)
        step = (step[0] + direction[0], step[1] + direction[1])

    return points


# %%
def solve_part_1(data: list) -> int:
    data = list(filter(lambda d: d[0][0] == d[1][0] or d[0][1] == d[1][1], data))

    points_hash = {}

    for (p1, p2) in data:
        points = get_points(p1, p2)
        for p in points:
            if p not in points_hash:
                points_hash[p] = 0
            points_hash[p] += 1

    overlaps = list(filter(lambda it: it[1] > 1, points_hash.items()))

    return len(overlaps)


print(solve_part_1(data))


# %%
def solve_part_2(data: list) -> int:
    points_hash = {}

    for (p1, p2) in data:
        points = get_points(p1, p2)
        for p in points:
            if p not in points_hash:
                points_hash[p] = 0
            points_hash[p] += 1

    overlaps = list(filter(lambda it: it[1] > 1, points_hash.items()))

    return len(overlaps)


print(solve_part_2(data))
