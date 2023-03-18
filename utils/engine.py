import random


def analyze_current_cell(curr_board, x, y):
    print(f"analyzing: {x}, {y}")
    print(curr_board[x][y])

    if curr_board[x][y] == 0:
        return None
    if curr_board[x][y] == "T":
        print(f"There's a trap! Oh no")
        return "T"
    else:
        print(f"Pick a card")
        curr_board[x][y] = 0
        return "C"


def START():
    return random.randint(0, 1)


def CHOICE(curr_board, choice, character):
    if choice == 4:
        print("Current player passed. ")
        return
    elif choice == 1:
        return analyze_current_cell(curr_board, character._get_pos_x(), character._get_pos_y())


def MOVE():
    x = -1
    y = -1

    while x < 0 or x > 15 or y < 0 or y > 15:
        x = int(input("Enter the row:   "))
        y = int(input("Enter the column:    "))

    return [x, y]


def END_TURN():
    print(f"Turn completed. Press ENTER to continue. . . ")
    input()
    print(f"=============================================")
