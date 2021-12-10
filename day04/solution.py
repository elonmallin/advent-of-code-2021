# %%
import os
import re
from functools import reduce

input_file = open(os.path.join(os.path.dirname(__file__), './input.txt'))

bingo_call_numbers = list(map(lambda l: int(l), input_file.readline().split(',')))
input_file.readline()  # Skip empty line

bingo_boards:list[list[int]] = []

while True:
    board = [
        *list(map(lambda l: int(l), re.split('\s+', input_file.readline().strip(' \n')))),
        *list(map(lambda l: int(l), re.split('\s+', input_file.readline().strip(' \n')))),
        *list(map(lambda l: int(l), re.split('\s+', input_file.readline().strip(' \n')))),
        *list(map(lambda l: int(l), re.split('\s+', input_file.readline().strip(' \n')))),
        *list(map(lambda l: int(l), re.split('\s+', input_file.readline().strip(' \n'))))
    ]
    bingo_boards.append(board)

    input_file.readline()

    pos = input_file.tell()
    if input_file.readline() == '':
        break
    input_file.seek(pos)

# %%
def gen_win_positions(size: int) -> list[int]:
    win_positions:list[int] = []

    for y in range(size):
        row = []
        col = []
        for x in range(size):
            row.append(y*size + x)
            col.append(y + x*size)
            
        win_positions.append(row)
        win_positions.append(col)

    return win_positions


def mark_board(board: list[int], n: int):
    for i, bn in enumerate(board):
        if bn == n:
            board[i] = -1 # Mark as checked
            break


def is_win(win_positions: list[int], board: list[int]) -> bool:
    for win_pos in win_positions:
        win = True
        for i in win_pos:
            if board[i] != -1:
                win = False
                break

        if win == True:
            return True

    return False


def calc_score(board: list[int], number_called: int) -> int:
    unmarked = filter(lambda i: i != -1, board)

    return sum(unmarked) * number_called


# %%
def solve_part_1(bingo_call_numbers: list[int], bingo_boards: list[list[int]]) -> int:
    win_positions = gen_win_positions(5)

    for number_called in bingo_call_numbers:
        for board in bingo_boards:
            mark_board(board, number_called)
            if is_win(win_positions, board):
                return calc_score(board, number_called)


print(solve_part_1(bingo_call_numbers, bingo_boards))


# %%
def solve_part_2(bingo_call_numbers: list[int], bingo_boards: list[list[int]]) -> int:
    win_positions = gen_win_positions(5)

    for number_called in bingo_call_numbers:
        for i in reversed(range(len(bingo_boards))):
            board = bingo_boards[i]
            mark_board(board, number_called)

            if is_win(win_positions, board):
                if len(bingo_boards) == 1:
                    return calc_score(board, number_called)

                bingo_boards.remove(board)


print(solve_part_2(bingo_call_numbers, bingo_boards))
