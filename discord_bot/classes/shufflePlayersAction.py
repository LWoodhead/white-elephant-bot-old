from .action import Action
from .game import Game
from .actionRecord import ActionRecord
import random
import copy

class ShufflePlayersAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int) -> ActionRecord:
        prevPlayerList = copy.deepcopy(game.get_player_list())
        game.shuffle_players()
        data = { "type": "shuffle", "prevPlayerList" : prevPlayerList}
        shuffle_record = ActionRecord(actionId,data)
        
        return shuffle_record

    def undo(self, game: Game, record: ActionRecord) -> None:
        game.set_player_list(record.data['prevPlayerList'])