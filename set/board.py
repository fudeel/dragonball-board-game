import random

from utils.game import game_state, save_game

board = [[0 for j in range(16)] for i in range(16)]


def generate_game_board():
    print("> Generating board... ")
    game_board = board

    # Put balls in map
    for i in range(5):
        while True:
            row = random.randint(0, 15)
            col = random.randint(0, 15)
            if game_board[row][col] == 0:
                game_board[row][col] = "X"
                break

    # Put cards in map
    for i in range(10):
        while True:
            row = random.randint(0, 15)
            col = random.randint(0, 15)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(16)]:
                game_board[row][col] = "C"
                break

    # Put traps in map
    for i in range(10):
        while True:
            row = random.randint(0, 15)
            col = random.randint(0, 15)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(16)] \
                    and "C" not in game_board[row] and "C" not in [game_board[r][col] for r in range(16)]:
                game_board[row][col] = "T"
                break

    game_state['board'] = game_board
    save_game(game_state, 'saved_game.json')

    return game_board
