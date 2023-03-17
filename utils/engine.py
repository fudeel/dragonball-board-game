import random

from utils.game import generate_game_board


game_board = generate_game_board()


def interact_with_cell(player_obj):
    cell = game_board[player_obj._get_pos_x()][player_obj._get_pos_y()]

    if cell == "T":
        print(f"Ouch! It was a trap! {player_obj._get_name()} loses 1 HP")
        player_obj._reduce_hp()

    elif cell == "X":
        print(f"Yes! {player_obj._get_name()} found a Dragon Ball sphere! If you already found one,"
              f"drop this in the same cell you drop the previous sphere otherwise choose a location with your team. ")
        player_obj._get_carrying_spheres(is_drop=False)
    elif cell == "C":
        print(f"{player_obj._get_name()} pick a card and use it wisely")
    else:
        print(f"{player_obj._get_name()} try somewhere else.")


tempo = 0
team_purple = []
team_orange = []

current_team = 0
current_orange = 0
next_orange = 0
current_player_obj = None


def START(purple, orange):
    global current_team
    global current_player_obj

    current_team = random.randint(0, 1)
    if current_team == 0:
        print("First move to Team Purple. Go Freezer!")
        current_player_obj = orange[0]

    else:
        current_team = 1
        global current_orange
        current_orange = 0
        print(f"First move to Team Orange. Go {orange[current_orange]._get_name()}!")
        current_player_obj = orange[0]

    global team_purple
    global team_orange

    team_purple = purple
    team_orange = orange

    while check_teams():
        for i in range(50):
            print("||")

        print(f"{print_current_team_and_player_name(current_team)}'s Turn!")
        action()
        move(current_team)
        for p in team_purple:
            print(f"Freezer: {p._get_hp()}")
            p.reduce_hp(1)

    print("Game ended")


def print_current_team_and_player_name(current):
    global current_orange
    if current == 0:
        return "Freezer"
    else:
        return team_orange[current_orange]._get_name()


def check_teams():
    for p in team_purple:
        if p._get_hp() > 0:
            return True
    return False


def move(current_team):
    global tempo
    if current_team == 0:
        current_player = team_purple[0]
    elif current_team == 1:
        current_player = team_orange[current_orange]

    confirm = ""
    while confirm != 'y':
        print(f"{current_player._get_name()}, roll a dice and insert the new ROW and COL in which you move")
        pos_x = int(input("Insert new ROW X:    "))
        pos_y = int(input("Insert new COL Y:    "))

        confirm = input(f"Confermi di spostarti su riga {pos_x} colonna {pos_y}? [y] / [n]").lower()

        if confirm == 'y':
            switch(current_team)
            tempo = tempo + 1


def action():
    action = ""

    while action != "interact" and action != "use card" and action != "pass":
        action = input("Cosa vuoi fare? [interact] [use card] [pass]").lower()

        if action == "interact":
            interact()

        if action == "use card":
            use_card()

        if action == "pass":
            pass_turn()


def switch(ct):
    global current_player_obj
    print(">    switching")
    if ct == 0:
        global current_team
        global current_orange
        global tempo
        current_team = 1
        if current_orange + 1 < len(team_orange) and tempo > 0:
            current_orange = current_orange + 1
            current_player_obj = team_orange[current_orange]
        else:
            current_orange = 0
            current_player_obj = team_orange[current_orange]
    else:
        current_team = 0
        current_player_obj = team_purple[0]


def interact():
    print(f"{print_current_team_and_player_name(current_team)} picks in the cell")
    print(f"Current player name: {current_team}")

    if current_team == 0:
        interact_with_cell(team_purple[0])
    else:
        interact_with_cell(team_orange[current_orange])
    return


def pass_turn():
    print(f"{print_current_team_and_player_name(current_team)} doesn't want to risk anything. He passes")
    return


def use_card():
    print(f"{print_current_team_and_player_name(current_team)} is brave enough to use a card!")
    return


def roll():
    print(f"{print_current_team_and_player_name(current_team)} rolls a dice")
    return
