import random


def interact_with_cell(board, player_name, pos_x, pos_y):
    cell = board[pos_x][pos_y]

    return f"{player_name} is interacting with {cell}"


round = 0
start = 0

team_purple = []
team_orange = []


def START(purple, orange):
    first = random.randint(0, 1)
    if first == 0:
        print("First move to Team Purple. Go Freezer!")

    else:
        print(f"First move to Team Orange. Go {orange[0]._get_name}!")
        global start
        start = 1

    global team_purple
    global team_orange

    team_purple = purple
    team_orange = orange

    while check_teams():
        for p in team_purple:
            print(f"Freezer: {p._get_hp()}")
            p.reduce_hp(1)

    print("Game ended")


def check_teams():
    for p in team_purple:
        if p._get_hp() > 0:
            return True
    return False
