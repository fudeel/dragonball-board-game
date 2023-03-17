import random


def interact_with_cell(board, player_name, pos_x, pos_y):
    cell = board[pos_x][pos_y]

    return f"{player_name} is interacting with {cell}"


def check_hp(team):
    for member in team:
        print(member._get_hp())
        if member._get_hp() > 0:
            return True
    return False


def check_teams(team_purple, team_orange):
    if check_hp(team_purple) and check_hp(team_orange):
        return True
    return False


round = 0
start = 0


def START(team_purple, team_orange):
    print("A")
    first = random.randint(0, 1)
    if first == 0:
        print("First move to Team Purple. Go Freezer!")

    else:
        print(f"First move to Team Orange. Go {team_orange[0]._get_name}!")
        global start
        start = 1

    while check_teams(team_purple, team_orange):
        team_purple[0].reduce_hp(1)
        team_orange[0].reduce_hp(1)
        team_orange[1].reduce_hp(1)

    print("Game ended")
