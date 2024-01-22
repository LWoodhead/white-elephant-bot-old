from .action import Action
from .game import Game
from .actionRecord import ActionRecord
import copy

class ShufflePlayersAction(Action):
    
    def __init__(self) -> None:
        super().__init__()
        
    def do(self, game: Game, actionId: int) -> ActionRecord:
        prevPassCount = game.get_pass_count()
        prevPlayerList = copy.deepcopy(game.get_player_list())
        prevIndex = game.get_current_player_index()
        
        game.shuffle_players()
        game.set_pass_count(0)
        game.set_current_player_index(0)
        
        data = { "type" : "shuffle", "prevPlayerList" : prevPlayerList, "prevPassCount" : prevPassCount,
                "prevIndex" : prevIndex}
        shuffle_record = ActionRecord(actionId,data)
        return shuffle_record
        
    #Sort the second list to match the order of the first
    #Both neeed to be the same size and have matching players
    @staticmethod   
    def mirror_list(listToMirror: [], targetList: []) -> []:
        for i in range(len(listToMirror)):
            for j in range(len(targetList)):
                if(listToMirror[i] == targetList[j]):
                    temp = targetList[i]
                    targetList[i] = targetList[j]
                    targetList[j] = temp
                    continue
                
    def undo(self, game: Game, record: ActionRecord) -> None:
        ShufflePlayersAction.mirror_list(record.data['prevPlayerList'], game.get_player_list())
        # game.set_player_list(record.data['prevPlayerList'])
        game.set_pass_count(record.data['prevPassCount'])
        game.set_current_player_index(record.data['prevIndex'])