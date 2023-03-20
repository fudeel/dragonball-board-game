import json

from models.character import Character
from utils.selection import character_selection

game_state = {}
teams = []


def save_game(state, filename):
    with open(filename, 'w') as f:
        json.dump(state, f)


def load_game(filename):
    with open(filename, 'r') as f:
        state = json.load(f)
    return state


def init():
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
                        carrying_spheres=0)
    team_purple = [freezer]
    teams.append(team_purple)
    team_orange = []
    print("Creating other players... ")

    remaining_players = num_of_players - 1
    while remaining_players > 0:
        team_orange.append(character_selection())
        remaining_players -= 1

    teams.append(team_orange)
