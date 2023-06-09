from colorama import init, Fore, Back, Style
from prettytable import PrettyTable

from models.colors import bcolors

init()

# Fore, Back and Style are convenience classes for the constant ANSI strings that set
#     the foreground, background and style. The don't have any magic of their own.
FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
STYLES = [Style.DIM, Style.NORMAL, Style.BRIGHT]

NAMES = {
    Fore.BLACK: 'black', Fore.RED: 'red', Fore.GREEN: 'green', Fore.YELLOW: 'yellow', Fore.BLUE: 'blue',
    Fore.MAGENTA: 'magenta', Fore.CYAN: 'cyan', Fore.WHITE: 'white'
    , Fore.RESET: 'reset',
    Back.BLACK: 'black', Back.RED: 'red', Back.GREEN: 'green', Back.YELLOW: 'yellow', Back.BLUE: 'blue',
    Back.MAGENTA: 'magenta', Back.CYAN: 'cyan', Back.WHITE: 'white',
    Back.RESET: 'reset'
}


def print_message(*args, **kwargs):
    if 'ct' in kwargs and kwargs['ct'] == 0 and 'end' not in kwargs:
        print(f"Current team: {Fore.MAGENTA} PURPLE {Fore.RESET} ")
    elif 'ct' in kwargs and kwargs['ct'] == 1 and 'end' not in kwargs:
        print(f"Current team: {bcolors.WARNING} ORANGE {Fore.RESET}")

    elif 'ct' in kwargs and kwargs['ct'] == 0 and 'end' in kwargs and kwargs['end'] == True:
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
        print(f"TEAM {bcolors.WARNING} ORANGE {Fore.RESET} HAS WON!")
    else:
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")
        print(f"TEAM {Fore.MAGENTA} PURPLE {Fore.RESET} HAS WON!")


def print_character(character):
    t = PrettyTable()
    t.field_names = ["Name", "HP", "Attack", "Defense", "AOE", "X", "Y"]
    t.add_row(
        [character._name, character._hp, character._attack, character._defense, character._basic_aoe, character._pos_x,
         character._pos_y])

    print(t)
