import random


def interact_with_cell(board, player_name, pos_x, pos_y):
    cell = board[pos_x][pos_y]

    return f"{player_name} is interacting with {cell}"


tempo = 0
team_purple = []
team_orange = []

current_team = 0
current_orange = 0
next_orange = 0


def START(purple, orange):
    global current_team
    current_team = random.randint(0, 1)
    if current_team == 0:
        print("First move to Team Purple. Go Freezer!")

    else:
        current_team = 1
        global current_orange
        current_orange = 0
        print(f"First move to Team Orange. Go {orange[current_orange]._get_name()}!")


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

    while action != "pick" and action != "use card" and action != "pass":
        action = input("Cosa vuoi fare? [pick] [use card] [pass]").lower()

        if action == "pick":
            pick()

        if action == "use card":
            use_card()

        if action == "pass":
            pass_turn()


def switch(ct):
    print(">    switching")
    if ct == 0:
        global current_team
        global current_orange
        global tempo
        current_team = 1
        if current_orange + 1 < len(team_orange) and tempo > 0:
            current_orange = current_orange + 1
        else:
            current_orange = 0
    else:
        current_team = 0


def pick():
    print(f"{print_current_team_and_player_name(current_team)} picks in the cell")
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
