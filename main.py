from typing import Union
from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from models.http_models import CreateGame

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
async def create_game(create_game: CreateGame):
    game_dict = dict(create_game)
    result = db["games"].insert_one(game_dict)
    return {"id": str(result.inserted_id)}