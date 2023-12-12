from .action import Action
from .game import Game
from .actionRecord import ActionRecord

class NoShuffleAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int) -> ActionRecord:
        prevPassCount = game.get_pass_count()
        prevIndex = game.get_current_player_index()
        
        game.set_pass_count(0)
        game.set_current_player_index(0)
        
        data = { "type" : "noShuffle", "prevPassCount" : prevPassCount, "prevIndex" : prevIndex}
        no_shuffle_record = ActionRecord(actionId,data)
        return no_shuffle_record

    def undo(self, game: Game, record: ActionRecord) -> None:
        game.set_pass_count(record.data['prevPassCount'])
        game.set_current_player_index(record.data['prevIndex'])