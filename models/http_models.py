from pydantic import BaseModel


class CreateGame(BaseModel):
    name: str
    is_started: bool = False
    num_of_players: int
    current_team: int = 0
    current_player: int = 0
    players: list = []
    gm: str = 'standard'
    game_round: int = 0
