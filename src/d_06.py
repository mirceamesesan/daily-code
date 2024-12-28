from random import randint as rd
from services.sudoku import Sudoku

input_rank = input(
    "Select your difficulty: (1) Easy, (2) Normal, (3) Difficult: "
)  # difficulty

if input_rank == "1":
    print("Easy")
    RANK = rd(10, 50)
elif input_rank == "2":
    print("Normal")
    RANK = rd(50, 100)
elif input_rank == "3":
    print("Difficult")
    RANK = rd(100, 150)

board = Sudoku(rank=RANK)

board.print_board()

board.solve()

print("\n\nSolved Sudoku:\n")

board.print_board()
