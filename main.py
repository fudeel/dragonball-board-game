import os
from models.character import Character
from utils.engine import START, CHOICE, END_TURN
from utils.game import init, load_game, generate_game_board, teams
from db import players

freezer = Character(name="Freezer",
                    basic_aoe=2,
                    attack=5,
                    energy=10,
                    defense=4,
                    hp=15,
                    pos_x=15,
                    pos_y=15,
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

teams = [team_purple, team_orange]

curr_team = START()

pi = 0  # purple index
oi = 0  # orange index

curr_board = generate_game_board()

print(curr_team)
if curr_team == 0:

    print(f"First team is Team Purple! ")

else:
    print(f"First team is Team Orange! ")


def game():
    if curr_team == 0:
        print(teams[curr_team][pi].__dict__)

        input(f"{teams[curr_team][pi]._name} roll a Dice")

        choice = int(input(f"What do you want to do?: \n [1] Analyze current cell \n "
                           f"[2] Attack a cell \n [3] Use a card \n [4] Pass"))

        if choice == 1 and CHOICE(curr_board, choice, teams[curr_team][pi]) is None:
            choice = 4

        if choice == 1 and CHOICE(curr_board, choice, teams[curr_team][pi]) == "T":
            print(f"There was a trap. {teams[curr_team][pi]._name} loses 1 HP")
            teams[curr_team][pi].reduce_hp(1)
            print(f"Updated {teams[curr_team][pi]._name}'s HP: {teams[curr_team][pi]._get_hp()}")
            choice = 4

        if choice == 1 and CHOICE(curr_board, choice, teams[curr_team][pi]) == "C":
            input(f"{teams[curr_team][pi]._name} picks a card")
            choice = 4

        if choice == 4:
            END_TURN()

    else:
        print(teams[curr_team][oi].__dict__)


game()
