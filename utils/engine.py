import random


def analyze_current_cell(curr_board, x, y):
    print(curr_board)
    print(f"analyzing: {x}, {y}")
    print(curr_board[x][y])

    if curr_board[x][y] == 0:
        return None
    if curr_board[x][y] == "T":
        print(f"There's a trap! Oh no")
        return "T"
    else:
        print(f"Pick a card")
        return "C"


def START():
    return random.randint(0, 1)


def CHOICE(curr_board, choice, character):
    if choice == 4:
        print("Current player passed. ")
        return
    elif choice == 1:
        return analyze_current_cell(curr_board, character._get_pos_x(), character._get_pos_y())


def END_TURN():
    print(f"Turn completed. Moving to next player. ")
    print(f"=============================================")
