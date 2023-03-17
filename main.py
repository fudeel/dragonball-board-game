from models.character import Character
import random
import os
from utils import engine
from utils.game import start, load_game, generate_game_board, save_game

game_state = {}

if os.path.exists('saved_game.json'):
    ans = None
    while ans != "y" and ans != "n":
        ans = (input("There is already a game saved. Do you want to load? y/N: ")).lower()

        if ans == "n":
            print("Good! You want a new adventure!")
            start()
            generate_game_board()

        elif ans == "y":
            game_state = load_game('saved_game.json')

            print(game_state)


else:
    # start a new game
    print("No game saved. Starting new game")
    start()