import os
import random

from models.character import Character
from utils.engine import START, round, start
from utils.game import init, load_game, generate_game_board, teams
from db import players

game_state = {}

if os.path.exists('saved_game.json'):
    ans = None
    while ans != "y" and ans != "n":
        ans = (input("There is already a game saved. Do you want to load? y/N: ")).lower()
        if ans == "n":
            print("Good! You want a new adventure!")
            init()
            generate_game_board()
            print(">    saving data on db... ")
            players.save_players(teams, "test")
        elif ans == "y":
            game_state = load_game('saved_game.json')

            print(game_state)
else:
    # start a new game
    print("No game saved. Starting new game")
    init()

freezer = Character(name="Freezer",
                    basic_aoe=2,
                    attack=5,
                    energy=10,
                    defense=4,
                    hp=15,
                    pos_x=31,
                    pos_y=31,
                    carrying_spheres=0)

goku = Character(
            name='Goku',
            pos_x=0,
            pos_y=0,
            defense=4,
            energy=8,
            attack=4,
            basic_aoe=2,
            carrying_spheres=0,
            hp=10
        )

crilin = Character(
            name='Crilin',
            pos_x=1,
            pos_y=0,
            defense=2,
            energy=10,
            attack=2,
            basic_aoe=1,
            carrying_spheres=0,
            hp=10
        )

team_purple = [freezer]
team_orange = [goku, crilin]


START(team_purple, team_orange)
