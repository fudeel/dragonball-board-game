import random
import secrets
import string

from pydantic import BaseModel


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(alphabet) for i in range(32))

    return random_string


class CreateGame(BaseModel):
    name: str
    game_id = generate_secret()
    is_started: bool = False
    num_of_players: int
    current_team: int = 0
    current_player: int = 0
    players: list = []
    gm: str = "standard"
    game_round: int = 0
    board = ""
