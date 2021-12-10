# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))
data = list(map(lambda l: l.strip('\n'), input_file.readlines()))


def make_bracket_table(parenthesis_val: int, square_val: int, curly_val: int, arrow_val: int) -> dict:
    return { ')': parenthesis_val, ']': square_val, '}': curly_val, '>': arrow_val }


def get_close_char(open_or_close_char: str) -> str:
    if open_or_close_char in ['(', ')']:
        return ')'
    elif open_or_close_char in ['[', ']']:
        return ']'
    elif open_or_close_char in ['{', '}']:
        return '}'
    elif open_or_close_char in ['<', '>']:
        return '>'


def get_open_char(open_or_close_char: str) -> str:
    if open_or_close_char in ['(', ')']:
        return '('
    elif open_or_close_char in ['[', ']']:
        return '['
    elif open_or_close_char in ['{', '}']:
        return '{'
    elif open_or_close_char in ['<', '>']:
        return '<'


def back_track(idx, open_char, line):
    brackets = make_bracket_table(0, 0, 0, 0)
    brackets[get_close_char(open_char)] += 1

    while idx >= 0:
        c = line[idx]
        close_c = get_close_char(c)
        brackets[close_c] += 1 if c == close_c else -1

        if brackets[close_c] < 0:
            return False
        if brackets[close_c] == 0 and open_char == c:
            return True

        idx -= 1

    return False


def lint_line(line: str, score_table: dict) -> int:
    brackets = make_bracket_table(0, 0, 0, 0)

    for i, c in enumerate(line):
        for pair in [['(', ')'], ['[', ']'], ['{', '}'], ['<', '>']]:
            if c == pair[0]:
                brackets[pair[1]] += 1
            elif c == pair[1]:
                if not back_track(i-1, pair[0], line):
                    return score_table[pair[1]]

    return 0


def solve_part_1(data: list[str]) -> int:
    score = 0
    score_table = make_bracket_table(3, 57, 1197, 25137)

    for line in data:
        score += lint_line(line, score_table)

    return score


print(solve_part_1(data))
