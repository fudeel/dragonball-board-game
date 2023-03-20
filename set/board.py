import random

from models.gamemode import GameMode
from utils.game import game_state, save_game

"""gamemodes that generate different map

[1] 16x16 / 7 spheres / 20 traps / 20 cards

"""


gm = GameMode(id=1, size=16, s=7, c=5, t=5)

print(f"{gm.size}")
board = [[0 for j in range(gm.size)] for i in range(gm.size)]


def ensure_numbers_of_elements(gb):
    char_count = {'C': 0, 'T': 0, 'X': 0}

    for row in gb:
        for char in row:
            if char in char_count:
                char_count[char] += 1

    print(f"Number of 'C's: {char_count['C']}")
    print(f"Number of 'T's: {char_count['T']}")
    print(f"Number of 'X's: {char_count['X']}")


def generate_game_board():
    """
    Function that generates a game board inserting Spheres, Cards and Traps on it. The number of elements
    depends on from the game mode settings.
    :return: game board with all elements in it
    """
    game_board = board

    # Put balls in map
    for i in range(gm.sphers):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if game_board[row][col] == 0:
                game_board[row][col] = "X"
                break

    # Put cards in map
    for i in range(gm.cards):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(gm.size - 1)]:
                game_board[row][col] = "C"
                break

    # Put traps in map
    for i in range(gm.traps):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(gm.size - 1)] \
                    and "C" not in game_board[row] and "C" not in [game_board[r][col] for r in range(gm.size - 1)]:
                game_board[row][col] = "T"
                break

    # ensure_numbers_of_elements(game_board)

    game_state['board'] = game_board
    save_game(game_state, 'saved_game.json')

    return game_board

