import hashlib
from typing import Union
from fastapi import FastAPI
from pandas._libs import json
from pymongo import MongoClient
from bson.json_util import dumps
from models.http_models import Game, Character, Player
from set.board import generate_game_board
from bson.objectid import ObjectId
import random

app = FastAPI()

client = MongoClient()
db = client["paragon-ball"]


@app.get("/")
def read_root():
    return {"PARAGON BALL - RAMECC"}


@app.get("/games")
async def get_games():
    """
    search for games in DB
    :return: games
    """
    games = db["games"].find({})
    return dumps(games)


@app.post("/games")
async def create_game(create_game: Game):
    """
    Crates a game on DB under the "games" collection using parameters from Client and generating hashed board
    :param create_game:
    :return:
    """
    game_dict = dict(create_game)
    board_json = json.dumps(generate_game_board())
    board_hash = hashlib.sha256(board_json.encode('utf-8')).hexdigest()

    game_dict['board'] = board_hash
    result = db["games"].insert_one(game_dict)

    return {"id": str(result.inserted_id)}


@app.get("/games/{game_id}")
async def get_game(game_id: str):
    # Query the document with the given ID from the games collection
    result = db["games"].find_one({'game_id': game_id}, {'_id': 0})

    # Return the result as a dictionary
    return result


@app.get("/characters")
async def get_characters():
    """
    search for games in DB
    :return: games
    """
    games = db["characters"].find({})
    return dumps(games)


@app.post("/characters")
async def create_character(create_character: Character):
    """
    Crates a game on DB under the "games" collection using parameters from Client and generating hashed board
    :param create_character:
    :return:
    """
    character_dict = dict(create_character)

    result = db["characters"].insert_one(character_dict)

    return {"id": str(result.inserted_id)}


@app.get("/games/{character_id}")
async def get_character(character_id: str):
    # Query the document with the given ID from the games collection
    result = db["characters"].find_one({'game_id': character_id}, {'_id': 0})

    # Return the result as a dictionary
    return result


@app.post("/players")
async def create_player(create_player: Player):
    """
    Crates a game on DB under the "games" collection using parameters from Client and generating hashed board
    :param create_player:
    :return:
    """
    player_dict = dict(create_player)

    result = db["players"].insert_one(player_dict)

    return {"id": str(result.inserted_id)}
