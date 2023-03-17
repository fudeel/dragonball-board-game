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

# Put traps in map
for i in range(12):
    while True:
        row = random.randint(0, 29)
        col = random.randint(0, 29)
        if board[row][col] == 0 and "X" not in board[row] and "X" not in [board[r][col] for r in range(30)] \
                and "C" not in board[row] and "C" not in [board[r][col] for r in range(30)]:
            board[row][col] = "T"
            break

goku = Character(name="Goku",
                 basic_aoe=2,
                 attack=4, energy=10,
                 defense=4,
                 hp=15,
                 pos_x=20,
                 pos_y=20,
                 is_carrying_dragonball=False)

freezer = Character(name="Freezer",
                    basic_aoe=4,
                    attack=5,
                    energy=10,
                    defense=4,
                    hp=15,
                    pos_x=20,
                    pos_y=20,
                    is_carrying_dragonball=False)


goku.interact_with_trap()

print(board)
print(goku)
print(freezer)