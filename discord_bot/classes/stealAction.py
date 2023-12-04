from .action import Action
from .game import Game
from .actionRecord import ActionRecord
from .player import Player

class StealAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int, stealer: Player, stolenFrom: Player) -> ActionRecord:
        temp_gift = stealer.gameGift
        stealer.gameGift = stolenFrom.gameGift
        stolenFrom.gameGift = temp_gift
        if(stolenFrom.gameGift != None):
            stolenFrom.gameGift.stolenCount += 1
        if(stealer.gameGift != None):
            stealer.gameGift.stolenCount += 1
        data = { "type" : "steal", "stealer" : stealer, "stolenFrom" : stolenFrom}    
        steal_record = ActionRecord(actionId,data)
        return steal_record
    
    def undo(self, game: Game, record: ActionRecord) -> None:
        stealer = record.data['stealer']
        stolenFrom = record.data['stolenFrom']
        
        temp_gift = stealer.gameGift
        stealer.gameGift = stolenFrom.gameGift
        stolenFrom.gameGift = temp_gift
        if(stolenFrom.gameGift != None):
            stolenFrom.gameGift.stolenCount -= 1
        if(stealer.gameGift != None):
            stealer.gameGift.stolenCount -= 1