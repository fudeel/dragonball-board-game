import json
import random

import set.board
from models.character import Character
from set import board
from utils.selection import character_selection
from utils.utils import toJSON

game_state = {}


def save_game(game_state, filename):
    with open(filename, 'w') as f:
        json.dump(game_state, f)


def load_game(filename):
    with open(filename, 'r') as f:
        game_state = json.load(f)
    return game_state


def start():
    print("Welcome to Namecc \n")
    num_of_players = 0
    while num_of_players < 2 or num_of_players > 5:
        num_of_players = int(input("Enter the number of players [min 2, max 5]: "))

    print(f"Preparing game for {num_of_players} players...")

    # team creation
    print("Creating freezer... ")
    freezer = Character(name="Freezer",
                        basic_aoe=2,
                        attack=5,
                        energy=10,
                        defense=4,
                        hp=15,
                        pos_x=31,
                        pos_y=31,
                        is_carrying_dragonball=False,
                        is_playing=True)
    team_purple = [freezer]
    team_orange = []
    print("Creating other players... ")

    remaining_players = num_of_players - 1
    while remaining_players > 0:
        team_orange.append(character_selection())
        remaining_players -= 1





def generate_game_board():
    print("> Generating board... ")
    game_board = board.board

    # Put balls in map
    for i in range(7):
        while True:
            row = random.randint(0, 31)
            col = random.randint(0, 31)
            if game_board[row][col] == 0:
                game_board[row][col] = "X"
                break

    # Put cards in map
    for i in range(20):
        while True:
            row = random.randint(0, 31)
            col = random.randint(0, 31)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(32)]:
                game_board[row][col] = "C"
                break

    # Put traps in map
    for i in range(12):
        while True:
            row = random.randint(0, 31)
            col = random.randint(0, 31)
            if game_board[row][col] == 0 and "X" not in game_board[row] \
                    and "X" not in [game_board[r][col] for r in range(32)] \
                    and "C" not in game_board[row] and "C" not in [game_board[r][col] for r in range(32)]:
                game_board[row][col] = "T"
                break

    print(game_board)

    game_state['board'] = game_board
    save_game(game_state, 'saved_game.json')


def continue_game(board, players):
    return