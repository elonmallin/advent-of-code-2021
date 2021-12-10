# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: (l.split(' | ')[0].split(' '), l.split(' | ')[1].strip('\n').split(' ')), input_file.readlines()))


# %%
def solve_part_1(data: list[(list[str], list[str])]) -> int:
    known_digit_lengths = [2, 4, 3, 7] # digits: 1, 4, 7, 8
    known_digit_count = 0

    for (signals, digits) in data:
        for digit in digits:
            if len(digit) in known_digit_lengths:
                known_digit_count += 1

    return known_digit_count


print(solve_part_1(data))


# %%
def contains_all(all, subset):
    return False not in [c in all for c in subset]


def subtract(s: str, sub: str) -> str:
    for x in sub:
        s = s.replace(x, '')

    return s


def analyze_signals(signals: str) -> dict:
    mapping = {
        1: ''.join(sorted(re.findall(r'\b(\w{2})\b', signals)[0])),
        4: ''.join(sorted(re.findall(r'\b(\w{4})\b', signals)[0])),
        7: ''.join(sorted(re.findall(r'\b(\w{3})\b', signals)[0])),
        8: ''.join(sorted(re.findall(r'\b(\w{7})\b', signals)[0])),
    }

    zeroAndSixAndNine = re.findall(r'\b(\w{6})\b', signals)
    for potentialNine in zeroAndSixAndNine:
        if contains_all(potentialNine, mapping[4]):
            # 4 is the only number that fits in 9
            mapping[9] = ''.join(sorted(potentialNine))
            break

    twoAndThreeAndFive = re.findall(r'\b(\w{5})\b', signals)
    for potentialThree in twoAndThreeAndFive:
        if contains_all(potentialThree, mapping[1]):
            # 1 is the only number that fits in 3
            mapping[3] = ''.join(sorted(potentialThree))
            break

    for potentialTwoAndFive in twoAndThreeAndFive:
        if ''.join(sorted(potentialTwoAndFive)) == mapping[3]:
            continue

        if len(subtract(potentialTwoAndFive, mapping[9])) == 1:
            mapping[2] = ''.join(sorted(potentialTwoAndFive))
        else:
            mapping[5] = ''.join(sorted(potentialTwoAndFive))

    for potentialZeroAndSix in zeroAndSixAndNine:
        if ''.join(sorted(potentialZeroAndSix)) == mapping[9]:
            continue

        if len(subtract(potentialZeroAndSix, mapping[5])) == 1:
            mapping[6] = ''.join(sorted(potentialZeroAndSix))
        else:
            mapping[0] = ''.join(sorted(potentialZeroAndSix))

    return { code: n for n, code in mapping.items() }


def decode_digits(digits: list[str], mapping: dict) -> int:
    s_builder = ''

    for digit in digits:
        s_builder += str(mapping[''.join(sorted(digit))])

    return int(s_builder)


def solve_part_2(data: list[(list[str], list[str])]) -> int:
    digit_sum = 0

    for (signals, digits) in data:
        mapping = analyze_signals(' '.join(signals))
        num = decode_digits(digits, mapping)
        digit_sum += num

    return digit_sum


print(solve_part_2(data))
