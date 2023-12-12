from .action import Action
from .game import Game
from .actionRecord import ActionRecord
from .player import Player

#Assuming that only someone with no game gift can open a gift

class OpenAction(Action):

    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int, 
           opener: Player, owner: Player) -> ActionRecord:
        target_gift = owner.get_original_gift()
        
        opener.set_game_gift(target_gift)
        target_gift.open()
        game.unopened_gift_count_down()
        game.player_index_up()
        
        data = { "type" : "open", "owner" : owner, "opener" : opener}
        open_record = ActionRecord(actionId,data)
        return open_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        opener = record.data['opener']
        owner = record.data['owner']
        
        opener.set_game_gift(None)
        owner.get_original_gift().close()
        game.unopened_gift_count_up()
        game.player_index_down()
        