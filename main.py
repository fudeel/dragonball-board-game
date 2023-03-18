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


def play(ct, cp):
    print(teams[ct][cp].__dict__)

    input(f"{teams[ct][cp]._name} roll a Dice")

    choice = int(input(f"What do you want to do?: \n [1] Analyze current cell \n "
                       f"[2] Attack a cell \n [3] Use a card \n [4] Pass"))

    if choice == 1 and CHOICE(curr_board, choice, teams[ct][cp]) is None:
        choice = 4

    if choice == 1 and CHOICE(curr_board, choice, teams[ct][cp]) == "T":
        print(f"There was a trap. {teams[ct][cp]._name} loses 1 HP")
        teams[ct][cp].reduce_hp(1)
        print(f"Updated {teams[ct][cp]._name}'s HP: {teams[ct][cp]._get_hp()}")
        choice = 4

    if choice == 1 and CHOICE(curr_board, choice, teams[ct][cp]) == "C":
        input(f"{teams[ct][cp]._name} picks a card")
        choice = 4

    if choice == 4:
        END_TURN()


def game():
    if curr_team == 0:
        ct = 0
        cp = 0

        play(ct, cp)

    else:
        ct = 1
        cp = 0

        play(ct, cp)


game()
