from .player import Player
from .template import Template
from .game import Game
from .shufflePlayersAction import ShufflePlayersAction
from .noShuffleAction import NoShuffleAction
from .passAction import PassAction
from .openAction import OpenAction
from .stealAction import StealAction
from .actionRecord import ActionRecord
from collections import deque

class GameWrapper():
    
    def __init__(self, gameId: int, config: Template, playerList: [Player]) -> None:
        
        self.gameObject = Game(gameId, config, playerList)
        self.playerList = playerList
        self.config = config
        
        #Object for creating a newRound 
        newRoundAction = None
        if(config.get_randomize_round_order() == True):
            newRoundAction = ShufflePlayersAction()
        else:
            newRoundAction = NoShuffleAction()
        self.newRound = newRoundAction
        
        #Create an empty stack for actions and actionId
        self.actionStack = deque()
        self.actionCounter = 0
    
        #Objects for each other action
        self.passAction = PassAction()
        self.openAction = OpenAction()
        self.stealAction = StealAction()
        
    #Action methods    
    def player_passes(self) -> None:
        self.actionCounter += 1
        actionId = self.actionCounter
        
        action_record = self.passAction.do(self.gameObject,actionId)
        self.actionStack.append(action_record)
    
    def player_opens(self, opener: Player, owner: Player) -> None:
        self.actionCounter += 1
        actionId = self.actionCounter
        
        action_record = self.openAction.do(self.gameObject,actionId,opener,owner)
        self.actionStack.append(action_record)
    
    def player_steals(self, stealer: Player, stolenFrom: Player) -> None:
        self.actionCounter += 1
        actionId = self.actionCounter
        
        action_record = self.stealAction.do(self.gameObject,actionId,stealer,stolenFrom)
        self.actionStack.append(action_record)
        
    # TODO Add veto action, should skip
    
    #Info Methods
    def is_game_over(self) -> bool:
        return self.gameObject.all_passed_end() or self.gameObject.players_locked_end()
    
    def new_round(self) -> None:
        self.actionCounter += 1
        actionId = self.actionCounter
        
        action_record = self.newRound.do(self.gameObject,actionId)
        self.actionStack.append(action_record)
        
    def pre_pass_end_check(self) -> bool:
        #TODO move this into a single method in game then call it here
        if(self.gameObject.get_pass_count() == self.gameObject.get_player_count() - 1):
            return True
        return False
        
    #Undoes the last steal/pass/open, will undo a round shuffle first if needed
    def undo_last_action(self) -> None:
        action_record = self.actionStack.pop()
        actionType = action_record.data['type']
        
        match actionType:
            case "pass":
                self.passAction.undo(self.gameObject,action_record)
            
            case "steal":
                self.stealAction.undo(self.gameObject,action_record)
                
            case "open":
                self.openAction.undo(self.gameObject,action_record)
                
            case "shuffle":
                self.newRound.undo(self.gameObject,action_record)
                self.undo_last_action()
                
            case "noShuffle":
                self.newRound.undo(self.gameObject,action_record)
                self.undo_last_action()
    
    def currentPlayer(self) -> Player:
        return self.gameObject[self.gameObject.currentPlayerIndex]
    
    #Validation Methods
    #TODO call these in action methods and add 0 or 1 as return types 
    def valid_pass(self) -> bool:
        if(self.gameObject.get_unopened_gift_count() != 0):
            return False
        return True

    def valid_open(self, opener: Player, owner: Player) -> bool:
        if(owner.originalGift.get_is_wrapped() == False or opener.get_game_gift() == None):
            return False
        return True
        
    def valid_steal(self, stealer: Player, stolenFrom: Player) -> bool:
        if(stolenFrom.get_game_gift() == None):
            return False
        return True
    
    def list_valid_actions(self) -> (bool,bool,bool):
        # TODO return a tuple with values for (can pass, can open, can steal)
        pass