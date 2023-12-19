from .action import Action
from .game import Game
from .actionRecord import ActionRecord
from .player import Player

class StealAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int, stealer: Player, 
           stolenFrom: Player) -> ActionRecord:
        stealerGift = stealer.get_game_gift()
        stolenFromGift = stolenFrom.get_game_gift()
        
        game.player_index_up()
        stealer.set_game_gift(stolenFromGift)
        stolenFrom.set_game_gift(stealerGift)
        if(stolenFromGift != None):
            stolenFromGift.steal()
            if(stolenFromGift.get_stolen_count() >= game.get_config().get_max_steals()):
                game.unlocked_player_count_down()
                stealer.set_locked(True)
        
        data = { "type" : "steal", "stealer" : stealer, "stolenFrom" : stolenFrom}    
        steal_record = ActionRecord(actionId,data)
        return steal_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        stealer = record.data['stealer']
        stolenFrom = record.data['stolenFrom']
        stealerGift = stealer.get_game_gift()
        stolenFromGift = stolenFrom.get_game_gift()
        
        #Decrement the index and swap the two gifts back
        game.player_index_down()
        stealer.set_game_gift(stolenFromGift)
        stolenFrom.set_game_gift(stealerGift)
        if(stealerGift != None):
            #Release the stolen gift to decrement the stolen counter
            stealerGift.release()
            #Check to see if this brings the player to an unlocked state
            if(stealerGift.get_stolen_count() == game.get_config().get_max_steals() - 1):
                game.unlocked_player_count_up()
                stealer.set_locked(False)