from .action import Action
from .game import Game
from .actionRecord import ActionRecord

class PassAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int) -> ActionRecord:
        game.pass_count_up()
        game.player_index_up()
        
        data = { "type": "pass" }
        pass_record = ActionRecord(actionId,data)
        return pass_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        game.pass_count_down()
        game.player_index_down()