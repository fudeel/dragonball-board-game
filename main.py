import copy
import random

from colorama import Fore

from models.character import Character
from models.colors import bcolors
from set.board import generate_game_board, gm
from utils.engine import START, END_TURN, MOVE, ATTACK, has_hp, search_card_information, ALIGN_SPHERES
from utils.game import teams
from utils.logprinter import print_message, print_character

freezer = Character(name="Freezer",
                    basic_aoe=3,
                    attack=5,
                    energy=10,
                    defense=4,
                    hp=15,
                    pos_x=15,
                    pos_y=15)

goku = Character(
    name='Goku',
    pos_x=0,
    pos_y=0,
    defense=4,
    energy=8,
    attack=4,
    basic_aoe=1,
    hp=8
)

vegeta = Character(
    name='Vegeta',
    pos_x=0,
    pos_y=1,
    defense=4,
    energy=8,
    attack=4,
    basic_aoe=1,
    hp=8
)

team_purple = [freezer]
team_orange = [goku, vegeta]

teams = [team_purple, team_orange]

curr_team = START()

pi = 0  # purple index
oi = 0  # orange index
pp = -1  # previous player in orange

game_round = 0  # init game round

gm = gm  # game mode contains all the board settings

curr_board = generate_game_board()  # game board that contains elements and players
curr_board_without_players = copy.deepcopy(curr_board)  # game board that contains elements only for easy replacements


def init_players_on_map(character, gm):
    """
    @:param character
    this function is used to put players on a map before the game starts. It ensures also that the players are
    being inserted in a cell that is not used for a Trap, Card or by another player"""

    player_is_ready = False
    while player_is_ready is not True:
        x = random.randint(0, gm.size - 1)
        y = random.randint(0, gm.size - 1)

        if isinstance(curr_board[x][y], Character) and curr_board[x][y] == 0:
            player_is_ready = False
            print("There's another element in this cell.")
        else:
            character.set_pos_x(x)
            character.set_pos_y(y)
            curr_board[x][y] = character
            player_is_ready = True


def play(ct, cp):
    global pp
    global game_round
    while has_hp(teams[0], teams[1]):

        # print(curr_board)
        # print(curr_board_without_players)

        print(f"====| GAME ROUND {game_round} |====")
        print_message(ct=ct)
        print("")

        if ct == 1 and pp == -1:
            pp = cp

        elif ct == 1 and pp > -1:
            cp = (pp + 1) % len(team_orange)

            if team_orange[cp]:
                pp += 1
            else:
                cp = 0
                pp = -1

        print_character(teams[ct][cp])
        print("")
        print(f"{teams[ct][cp]._name} roll a Dice and move around the map to find the Dragon Balls")

        is_move_valid = False

        """ Move the player and update the Board by inserting the new player's position. If the player leaves a cell that
        contains a card [C] or a sphere [S] without interacting with it, the board_without_players re-inserts the cell's value on the
        main board"""

        while not is_move_valid:
            x, y = MOVE()

            if isinstance(curr_board[x][y], Character):
                is_move_valid = False
                print("There's already another player in this position")
            else:
                is_move_valid = True

        curr_board[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] = \
            curr_board_without_players[teams[ct][cp].get_pos_x()][
                teams[ct][cp].get_pos_y()]  # restoring cards or spheres


        teams[ct][cp].set_pos_x(x)
        teams[ct][cp].set_pos_y(y)
        curr_board[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] = teams[ct][cp]

        """ Player makes a choice """

        choice = 0
        while choice != 1 or choice != 2 or choice != 3 or choice != 4:

            try:

                choice = int(input(f"What do you want to do?: \n [1] Analyze current cell \n "
                                   f"[2] Attack a cell \n [3] Drop sphere \n [4] Pass"))

                if choice == 1:
                    if curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] == 'C':
                        # player picks a card and enters its number on the system
                        print(f"{teams[ct][cp].get_name()} found a card! Pick the card and insert its value")
                        # card_id = int(input(f"Card's number:  "))
                        curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] = 0

                        # collected_card = search_card_information(card_id)
                        # teams[ct][cp].set_cards(collected_card)
                        # print(f"{teams[ct][cp].get_name()} collected {Fore.CYAN}{collected_card.get_name()}{Fore.RESET}")
                        END_TURN()
                    elif curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] == 'T':
                        # player gets damage from a trap
                        print(f"Oh no! It was a trap! {teams[ct][cp].get_name()}'s HP reduced by {Fore.RED} 1 {Fore.RESET}")
                        teams[ct][cp].reduce_hp(1)
                        END_TURN()
                    elif curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] == "S":
                        # player discovered a Dragonball sphere
                        print(f"YES! {teams[ct][cp].get_name()} has found a Dragon Ball sphere!")
                        teams[ct][cp].set_carrying_spheres(True)
                        curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] = 0
                        END_TURN()
                    else:
                        END_TURN()
                        pass

                if choice == 2:
                    xs, ys = ATTACK(teams[ct][cp])  # rows and columns arrays
                    sorted_xs = sorted(xs)  # sorting from smaller to greater
                    sorted_ys = sorted(ys)  # sorting from smaller to greater

                    row_cells_to_attack = []  # rows within area init
                    columns_cells_to_attack = []  # columns within area init

                    # Iterate through the range of numbers between the first and second elements of `array`
                    for i in range(sorted_xs[0], sorted_xs[1] + 1):
                        # Append each number to `array_2`
                        row_cells_to_attack.append(i)

                    for i in range(sorted_ys[0], sorted_ys[1] + 1):
                        # Append each number to `array_2`
                        columns_cells_to_attack.append(i)

                    # attack
                    for i in row_cells_to_attack:
                        for j in columns_cells_to_attack:
                            if curr_board[i][j] == "T":
                                print("Destroyed a Trap!")
                                curr_board[i][j] = 0

                            if isinstance(curr_board[i][j], Character):
                                enemy_def = curr_board[i][j].get_defense()
                                player_att = teams[ct][cp].get_attack()

                                damage = player_att - enemy_def

                                if damage <= 0:
                                    damage = 1
                                print(
                                    f"{teams[ct][cp].get_name()} hits {curr_board[i][j].get_name()} and deals {damage} damage")
                                curr_board[i][j].reduce_hp(damage)

                    END_TURN()

                if choice == 3 and teams[ct][cp].get_carrying_spheres() is True:
                    if curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] == 0:
                        print("BOMB DROPPED")
                        curr_board_without_players[teams[ct][cp].get_pos_x()][teams[ct][cp].get_pos_y()] = "S"

                        aligned = ALIGN_SPHERES(curr_board_without_players, teams[ct],
                                                curr_board_without_players[teams[ct][cp].get_pos_x()],
                                                curr_board_without_players[teams[ct][cp].get_pos_y()], (gm.size - 1))

                        if aligned is True:
                            print(f"GAME ENDED")
                            if curr_team == 0:
                                print(f"Team {Fore.MAGENTA}PURPLE{Fore.RESET} has won!")
                                print(f"Team {Fore.MAGENTA}PURPLE{Fore.RESET} has won!")
                                print(f"Team {Fore.MAGENTA}PURPLE{Fore.RESET} has won!")
                                print(f"Team {Fore.MAGENTA}PURPLE{Fore.RESET} has won!")
                                return True
                            else:
                                print(f"Team {bcolors.WARNING}ORANGE{Fore.RESET} has won!")
                                print(f"Team {bcolors.WARNING}ORANGE{Fore.RESET} has won!")
                                print(f"Team {bcolors.WARNING}ORANGE{Fore.RESET} has won!")
                                print(f"Team {bcolors.WARNING}ORANGE{Fore.RESET} has won!")
                                return True

                    else:
                        print("Ops! You can't leave it here! Pay attention on the next turn \n")
                        END_TURN()
                elif choice == 3 and teams[ct][cp].get_carrying_spheres() is False:
                    print("You're not carrying any Dragonball Sphere. Pay attention on your next turn")
                    END_TURN()
                else:
                    break
                #    if teams[ct][cp].get_card_slot_1() is None or teams[ct][cp].get_card_slot_2() is None:
                #        print("use card")
                #        card_id = int(input("Insert the card you want to use:     "))
                #        selected_card = teams[ct][cp].get_card_by_id(card_id)
                #
                #        print(f"Selected card: {selected_card.get_name()}")
                #
                #        if selected_card.get_target() == "me":
                #            effect = selected_card.use_card()[0]
                #            attribute = effect[0]
                #            qty = effect[1]
                #            duration = selected_card.get_duration()
                #
                #            print(attribute)
                #            print(qty)
                #
                #            if attribute == 'attack':
                #                current_attack = teams[ct][cp].get_attack()
                #                tot = current_attack + qty
                #                print(tot)
                #                teams[ct][cp].set_attack(tot)
                #
                #            if teams[ct][cp].get_card_slot_1() is None:
                #                teams[ct][cp].set_card_slot_1(selected_card)
                #                teams[ct][cp].set_card_slot_1_duration(duration)
                #            else:
                #                teams[ct][cp].set_card_slot_2(selected_card)
                #                teams[ct][cp].set_card_slot_2_duration(duration)
                #        print("card used successfully")
                #        print_character(teams[ct][cp])

                if choice == 4:
                    END_TURN()

                if ct == 0:
                    ct = 1
                    break
                else:
                    ct = 0
                    cp = 0
                    break
            except:
                print("Enter valid choice")

        game_round += 1

        for i in range(50):
            print("")


def game():
    print("Putting players on the board...")

    for i in team_purple:
        init_players_on_map(i, gm)

    for i in team_orange:
        init_players_on_map(i, gm)

    if curr_team == 0:
        ct = 0
        cp = 0

        play(ct, cp)

    else:
        ct = 1
        cp = 0

        play(ct, cp)


game()

print("GAME ENDED.")
input("Press ENTER to close. . . ")
