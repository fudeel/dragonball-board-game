import random
import secrets
import string

from pydantic import BaseModel


def generate_secret():
    alphabet = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(alphabet) for i in range(32))

    return random_string


class Game(BaseModel):
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


class Character(BaseModel):
    character_id: str
    name: str
    hp: int
    level: int = 0
    attack: int
    defense: int
    aoe: int
    pos_x: int = 0
    pos_y: int = 0
    owner: str = ""


class Player(BaseModel):
    player_id: str = generate_secret()
    name: str
    game_id: str
    character_id: str
