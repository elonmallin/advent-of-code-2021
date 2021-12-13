# %%
import os
import re
from functools import reduce
import math

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

def parse_input(input_file) -> tuple[list[tuple[int, int]], list[tuple[str, int]]]:
    positions = []
    folds = []

    for line in input_file.readlines():
        if re.match('\d+,\d+', line):
            (x, y) = re.findall('(\d+),(\d+)', line)[0]
            positions.append((int(x), int(y)))
        elif line.startswith('fold'):
            (x_or_y, n) = re.findall('(x|y)=(\d+)', line)[0]
            folds.append((x_or_y, int(n)))

    return (positions, folds)


data = parse_input(input_file)


def build_paper(positions: list[tuple[int, int]]) -> list[list[int]]:
    (width, height) = reduce(lambda acc, p: (max(acc[0], p[0]), max(acc[1], p[1])), positions, (0, 0))

    pos_dict = { (p[0], p[1]): 0 for p in positions } # Speed up the pos lookup in the list comprehension

    paper = [[1 if (x, y) in pos_dict else 0 for x in range(width+1)] for y in range(height+1)]

    return paper


def fold_paper(paper: list[list[int]], fold: tuple[str, int]) -> list[list[int]]:
    if fold[0] == 'x':
        left = [[paper[y][x] for x in range(0, fold[1])] for y in range(len(paper))]
        right = [list(reversed([paper[y][x] for x in range(fold[1] + 1, len(paper[0]))])) for y in range(len(paper))]

        # Merge lists, only center folds exist in input
        if len(left) == len(right):
            paper = [[min(1, left[y][x] + right[y][x]) for x in range(len(left[0]))] for y in range(len(left))]

    elif fold[0] == 'y':
        top = [[paper[y][x] for x in range(len(paper[0]))] for y in range(0, fold[1])]
        bottom = list(reversed([[paper[y][x] for x in range(len(paper[0]))] for y in range(fold[1] + 1, len(paper))]))

        # Merge lists, only center folds exist in input
        if len(top) == len(bottom):
            paper = [[min(1, top[y][x] + bottom[y][x]) for x in range(len(top[0]))] for y in range(len(top))]

    return paper


def solve_part_1(data: tuple[list[tuple[int, int]], list[tuple[str, int]]]) -> int:
    (positions, folds) = data
    paper = build_paper(positions)

    paper = fold_paper(paper, folds[0])
    dot_count = reduce(lambda acc, l: acc + sum(l), paper, 0)

    return dot_count


print(solve_part_1(data))


def solve_part_2(data: tuple[list[tuple[int, int]], list[tuple[str, int]]]) -> str:
    (positions, folds) = data
    paper = build_paper(positions)

    for fold in folds:
        paper = fold_paper(paper, fold)

    return reduce(lambda acc, l: acc + ''.join('#' if i == 1 else ' ' for i in l) + '\n', paper, '')


print(solve_part_2(data))
