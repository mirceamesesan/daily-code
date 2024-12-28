from dokusan import generators
import numpy as np
from random import randint as rand

SIZE = 9
input_rank = input("Select your difficulty: (1) Easy, (2) Normal, (3) Difficult: ")  # difficulty

if input_rank == '1':
    print('Easy')
    RANK = rand(10, 50)
elif input_rank == '2':
    print('Normal')
    RANK = rand(50, 100)
elif input_rank == '3':
    print('Difficult')
    RANK = rand(100, 150)

    
dokusan_array = generators.random_sudoku(avg_rank=RANK)
dokusan_array_int = [int(row) for row in str(dokusan_array)]
dokusan_board = np.array(dokusan_array_int).reshape(SIZE, SIZE).tolist()


def solve(board):
    """Solving the board"""

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, SIZE + 1):
        if valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board: list, num: int, pos: tuple):
    """Checking the validity of the board: row, column and square"""
    # Checking the row
    for col in range(len(board[0])):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Checking the column
    for row in range(len(board)):
        # looping through each row
        if board[row][pos[1]] == num and pos[0] != row:
            return False

    # Checking the square of 3 x 3 where in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Looping through each square to check we don't have same num twice
    for square_y in range(box_y * 3, box_y * 3 + 3):
        for square_x in range(box_x * 3, box_x * 3 + 3):
            if board[square_y][square_x] == num and (square_y, square_x) != pos:
                return False

    return True


def print_board(board: list):
    """Printing the board in a more visible way"""
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("-----------------------")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def find_empty(board: list):
    """Finding the empty square"""
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)  # returning row and column
    return None


print_board(dokusan_board)

solve(dokusan_board)

print('\n\nSolved Sudoku:\n')

print_board(dokusan_board)
