from .action import Action
from .game import Game
from .actionRecord import ActionRecord

class PassAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int) -> ActionRecord:
        prevIndex = game.get_current_player_index()
        game.set_current_player_index(prevIndex+1)
        game.pass_count_up()
        data = { "type": "pass", "lastPlayerIndex": prevIndex }
        pass_record = ActionRecord(actionId,data)
        
        return pass_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        game.pass_count_down()
        game.set_current_player_index(record.data['lastPlayerIndex'])