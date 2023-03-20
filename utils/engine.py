import random

from utils.logprinter import print_message


def analyze_current_cell(curr_board, x, y):
    print(f"{x}, {y}")
    if curr_board[x][y] == 0:
        return None
    if curr_board[x][y] == "T":
        print(f"There's a trap! Oh no")
        return "T"
    elif curr_board[x][y] == "C":
        print(f"Pick a card")
        return "C"

    else:
        return


def has_hp(team_purple, team_orange):
    # Check if arr1 has an element with hp > 0
    has_hp_arr1 = any(element.get_hp() > 0 for element in team_purple)
    if not has_hp_arr1:
        print_message(ct=0, end=True)
        return False

    # Check if arr2 has an element with hp > 0
    has_hp_arr2 = any(element.get_hp() > 0 for element in team_orange)
    if not has_hp_arr2:
        print_message(ct=1, end=True)
        return False

    # Return True if both arrays have an element with hp > 0
    print("Both teams are playing")
    return has_hp_arr1 and has_hp_arr2


def START():
    """
    Tells which team starts first
    :return:
    """
    return random.randint(0, 1)


def CHOICE(curr_board, choice, character):
    if choice == 4:
        print("Current player passed. ")
        return
    elif choice == 1:
        if curr_board[character.get_pos_x()][character.get_pos_y()] == 'C':
            return "C"
        elif curr_board[character.get_pos_x()][character.get_pos_y()] == 'T':
            return "T"
        elif curr_board[character.get_pos_x()][character.get_pos_y()] == "S":
            return "S"
        else:
            return 0


def MOVE():
    x = -1
    y = -1

    while x < 0 or x > 15 or y < 0 or y > 15:
        x = int(input("Enter the row:   "))
        y = int(input("Enter the column:    "))

    return [x, y]


def ATTACK(attacker=None):
    x = -1
    y = -1

    while x < 0 or x > 15 or y < 0 or y > 15:
        x = int(input("Enter the row to attack:   "))
        y = int(input("Enter the column to attack:    "))

    xs = []
    ys = []

    print(f"attacker has {attacker._basic_aoe} AOE.")

    if x * attacker._basic_aoe <= 15:
        xs.append(x)
        xs.append((x + (1 * attacker._basic_aoe)) - 1)
    else:
        xs.append(x)
        xs.append((x - (1 * attacker._basic_aoe)) + 1)

    if y * attacker._basic_aoe <= 15:
        ys.append(y)
        ys.append((y + (1 * attacker._basic_aoe)) - 1)
    else:
        ys.append(y)
        ys.append((y - (1 * attacker._basic_aoe)) + 1)

    print(f"attacking {xs} {ys}")

    return [xs, ys]


def END_TURN():
    print(f"Turn completed. Press ENTER to continue. . . ")
    input()
    print(f"=============================================")
