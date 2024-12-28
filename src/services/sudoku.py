from dataclasses import dataclass
import numpy as np
from dokusan import generators
from typing import Optional


@dataclass
class Board:
    """Board class to generate the sudoku board"""

    rank: int = 100
    size: Optional[int] = 9

    def generate_board(self):
        dokusan_array = generators.random_sudoku(avg_rank=self.rank)
        dokusan_array_int = [int(row) for row in str(dokusan_array)]
        generated = np.array(dokusan_array_int).reshape(9,9).tolist()
        return generated


class Sudoku(Board):
    """Sudoku class to solve the board"""

    def __init__(self, rank: int):
        self.rank = rank
        self.board = self.generate_board()

    def solve(self):
        """Solving the board"""
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, self.size + 1):
            if self.valid(i, (row, col)):
                self.board[row][col] = i
                if self.solve():
                    return True

                self.board[row][col] = 0

        return False

    def find_empty(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def valid(self, num: int, pos: tuple):
        """Checking the validity of the board: row, column and square"""
        # Checking the row
        for col in range(self.size):
            if self.board[pos[0]][col] == num and pos[1] != col:
                return False

        # Checking the column
        for row in range(self.size):
            # looping through each row
            if self.board[row][pos[1]] == num and pos[0] != row:
                return False

        # Checking the square of 3 x 3 where in
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        # Looping through each square to check we don't have same num twice
        for square_y in range(box_y * 3, box_y * 3 + 3):
            for square_x in range(box_x * 3, box_x * 3 + 3):
                if (
                    self.board[square_y][square_x] == num
                    and (square_y, square_x) != pos
                ):
                    return False

        return True

    def print_board(self):
        """Printing the board in a more visible way"""
        for row in range(len(self.board)):
            if row % 3 == 0 and row != 0:
                print("---------------------")

            for col in range(len(self.board[0])):
                if col % 3 == 0 and col != 0:
                    print("| ", end="")

                if col == 8:
                    print(self.board[row][col])
                else:
                    print(str(self.board[row][col]) + " ", end="")
