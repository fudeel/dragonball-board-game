from models.character import Character
from set import dices, board
import random

print(dices.roll_dice())
board = board.board

# Put balls in map
for i in range(7):
    while True:
        row = random.randint(0, 29)
        col = random.randint(0, 29)
        if board[row][col] == 0:
            board[row][col] = "X"
            break

# Put cards in map
for i in range(20):
    while True:
        row = random.randint(0, 29)
        col = random.randint(0, 29)
        if board[row][col] == 0 and "X" not in board[row] and "X" not in [board[r][col] for r in range(30)]:
            board[row][col] = "C"
            break


# Put cards in map
for i in range(12):
    while True:
        row = random.randint(0, 29)
        col = random.randint(0, 29)
        if board[row][col] == 0 and "X" not in board[row] and "X" not in [board[r][col] for r in range(30)] \
                and "C" not in board[row] and "C" not in [board[r][col] for r in range(30)]:
            board[row][col] = "T"
            break

goku = Character('Goku', 3, 4, 15, 10, False, 2, 20, 20)
freezer = Character('Freezer', 5, 5, 15, 10, False, 4, 20, 4)

print(board)
print(goku)
print(freezer)
