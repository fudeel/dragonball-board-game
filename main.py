from set import dices, board
import random

print(dices.roll_dice())
board = board.board

# Put balls in map
for i in range(7):
    while True:
        row = random.randint(0, 30)
        col = random.randint(0, 30)
        if board[row][col] == 0:
            board[row][col] = "X"
            break

# Put Pick Cards in map
for i in range(20):
    while True:
        row = random.randint(0, 30)
        col = random.randint(0, 30)
        if board[row][col] == 0 and "X" not in board[row] and "X" not in [board[r][col] for r in range(30)]:
            board[row][col] = "C"
            break


print(board)