import random


def interact_with_cell(board, player_name, pos_x, pos_y):
    cell = board[pos_x][pos_y]

    return f"{player_name} is interacting with {cell}"


round = 0
team_purple = []
team_orange = []

current = 0
current_orange = 0


def START(purple, orange):
    global current
    current = random.randint(0, 1)
    if current == 0:
        print("First move to Team Purple. Go Freezer!")

    else:
        current = 1
        global current_orange
        current_orange = 0
        print(f"First move to Team Orange. Go {orange[current_orange]._get_name()}!")

    global team_purple
    global team_orange

    team_purple = purple
    team_orange = orange

    while check_teams():
        action()
        move(current)
        for p in team_purple:
            print(f"Freezer: {p._get_hp()}")
            p.reduce_hp(1)

    print("Game ended")


def check_teams():
    for p in team_purple:
        if p._get_hp() > 0:
            return True
    return False


def move(current_team):
    if current_team == 0:
        current_player = team_purple[0]
    elif current_team == 1:
        current_player = team_orange[current_orange]

    confirm = ""
    while confirm != 'y':
        print(f"{current_player._get_name()}, lancia il dado e inserisci la nuova posizione in cui ti sposti")
        pos_x = int(input("Insert new X:    "))
        pos_y = int(input("Insert new Y:    "))

        confirm = input(f"Confermi di spostarti su riga {pos_x} colonna {pos_y}? [y] / [n]").lower()

        if confirm == 'y':
            swap(current_team)


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


def swap(ct):
    if ct == 0:
        global current
        current = 1
    else:
        current = 0


def pick():
    print("Pick a card")
    return


def pass_turn():
    print("You passed")
    return


def use_card():
    print("Use a card")
    return


def roll():
    print("Roll dice")
    return
