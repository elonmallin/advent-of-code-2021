# %%
import os
import re
from functools import reduce
import math
from collections import Counter

input_file = open(os.path.join(os.path.dirname(__file__), './in.txt'))

template = input_file.readline().strip()
input_file.readline()
pair_insertions: dict[str, str] = {}

for line in input_file.readlines():
    (k, v) = line.strip().split(' -> ')
    pair_insertions[k] = v


# %%
def step(template: str, pair_insertions: dict[str, str]):
    new_template = ''

    for i in range(len(template) - 1):
        pair_key = template[i] + template[i+1]
        if pair_key in pair_insertions:
            new_template += template[i] + pair_insertions[pair_key]
        else:
            new_template += template[i]

        if i == len(template) - 2:
            new_template += template[i+1]

    return new_template


def solve_part_1(template: str, pair_insertions: dict[str, str]) -> int:
    for _ in range(10):
        template = step(template, pair_insertions)

    freq = Counter(template)
    commons = freq.most_common(len(freq))
    n_min = commons[-1][1]
    n_max = commons[0][1]

    return n_max - n_min


print(solve_part_1(template, pair_insertions))


# %%
# Part 2 not done, need completely different non naive solution
def step2(template: str, pair_insertions: dict[str, str], memo: dict[str, str], memo_longest_key: int):
    new_template = ''
    template_delta = ''
    template_len = len(template)

    i = 0
    while i < template_len - 1:
        memo_key = template[0:i+1]
        if i > 1 and memo_key not in memo:
            memo_longest_key = max(memo_longest_key, i+1)
            memo[memo_key] = new_template
            
        memo_used = False

        for j in range(min(template_len-1, memo_longest_key), i, -1):
            if template[i:j] in memo:
                mk = template[i:j]
                mv = memo[mk]
                new_template += mv
                memo_used = True
                i += len(mk)-1 # Probably -1 since we need to eval the last c in mk with c idx+1
                break

        if memo_used:
            continue

        pair_key = template[i] + template[i+1]
        if pair_key in pair_insertions:
            template_delta = template[i] + pair_insertions[pair_key]
            new_template += template_delta
        else:
            template_delta = template[i]
            new_template += template[i]

        if i == len(template) - 2:
            template_delta = template[i+1]
            new_template += template[i+1]

        i += 1

    memo[template] = new_template

    return new_template, memo_longest_key


def solve_part_2(template: str, pair_insertions: dict[str, str]) -> int:
    memo = {
        'NNC': 'NCNB'
    }
    memo_longest_key = len(template)

    for _ in range(15):
        template, memo_longest_key = step2(template, pair_insertions, memo, memo_longest_key)

    freq = Counter(template)
    commons = freq.most_common(len(freq))
    n_min = commons[-1][1]
    n_max = commons[0][1]

    return n_max - n_min


print(solve_part_2(template, pair_insertions))
