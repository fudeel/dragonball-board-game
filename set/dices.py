import random


def roll_dice(n = 1):
    if n < 2:
        return random.randint(1, 6)
    elif n == 2:
        a = random.randint(1, 6)
        b = random.randint(1, 6)

        return a, b
    else:
        return "You can use only 2 set"


