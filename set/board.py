import random

from models.gamemode import GameMode
from set.cards import generate_cards
from utils.game import game_state, save_game

# game-modes that generate different map [1] 16x16 / 7 spheres / 20 traps / 20 cards
cards = generate_cards()

gm = GameMode(id=1, size=16, s=50, c=0, t=0)


def ensure_numbers_of_elements(gb):
    """
    This function is used to count elements on board, to ensure if the initialization puts the correct elements on it.
    :param gb:
    :return:
    """
    char_count = {'C': 0, 'T': 0, 'S': 0, 0: 0}

    for row in gb:
        for char in row:
            if char in char_count:
                char_count[char] += 1

    print(f"Number of 'C's: {char_count['C']}")
    print(f"Number of 'T's: {char_count['T']}")
    print(f"Number of 'S's: {char_count['S']}")
    print(f"Number of '0's: {char_count[0]}")


def generate_game_board():
    """
    Function that generates a game board inserting Spheres, Cards and Traps on it. The number of elements
    depends on from the game mode settings.
    :return: game board with all elements in it
    """
    
    board = [[0 for j in range(gm.size)] for i in range(gm.size)]

    # Put balls in map
    for i in range(gm.sphers):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if board[row][col] == 0 and board[row][col] != "S":
                board[row][col] = "S"
                break

    # Put cards in map
    for i in range(gm.cards):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if board[row][col] == 0 and board[row][col] != "S" and board[row][col] != "C":
                board[row][col] = "C"
                break

    # Put traps in map
    for i in range(gm.traps):
        while True:
            row = random.randint(0, gm.size - 1)
            col = random.randint(0, gm.size - 1)
            if board[row][col] == 0 and board[row][col] != "S" and board[row][col] != "C" and board[row][col] != "T":
                board[row][col] = "T"
                break

    ensure_numbers_of_elements(board)

    game_state['board'] = board
    save_game(game_state, 'saved_game.json')

    return board
