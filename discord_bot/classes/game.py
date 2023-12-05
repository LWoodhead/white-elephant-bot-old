from .player import Player
from .template import Template
from typing import Final
import random
import copy

class Game:
    
    def __init__(self, id: int, config: Template, playerList: [Player]) -> None:
        self.id = id
        self.config = config
        self.playerList = playerList
        self.currentPlayerIndex = 0
        self.passCount = 0
        self.unlockedPlayerCount = len(self.playerList)
        self.playerCount: Final = len(self.playerList)
        self.unopenedGiftCount = len(self.playerList)
        
    def __str__(self) -> str:
        result = "(id: %d, current player index: %d, pass count: %d, locked player count: %d, player count: %d\n)" %(
            self.id, self.currentPlayerIndex, self.passCount, self.lockedPlayerCount, self.playerCount
        )
        
        result += "**Players**\n"
        for player in self.playerList:
            result += str(player) + "\n"
            
        result += "**Template**\n"
        result += str(self.config)
        return result
        
    def get_id(self) -> int:
        return self.id
    
    def get_config(self) -> Template:
        return self.config
    
    def get_player_list(self) -> [Player,Player]:
        return self.playerList
    
    def set_player_list(self, newPlayerList: [Player, Player]) -> None:
        self.playerList = newPlayerList
    
    def get_current_player_index(self) -> int:
        return self.currentPlayerIndex
    
    def set_current_player_index(self,newIndex: int) -> None:
        if(newIndex >= self.playerCount or newIndex < 0):
            newIndex = 0
        self.currentPlayerIndex = newIndex
    
    def get_pass_count(self) -> int:
        return self.passCount
        
    def set_pass_count(self, newPassCount: int) -> None:
        if(newPassCount < 0):
            newPassCount = 0
        self.passCount = newPassCount
        
    def get_unlocked_player_count(self) -> int:
        return self.unlockedPlayerCount
    
    def set_unlocked_player_count(self, newUnlockedPlayerCount: int) -> int:
        if(newUnlockedPlayerCount < 0):
            newUnlockedPlayerCount = 0
        self.unlockedPlayerCount = newUnlockedPlayerCount
        
    def get_unopened_gift_count(self) -> int:
        return self.unopenedGiftCount
    
    def set_unopened_gift_count(self, newUnopenedGiftCount: int) -> None:
        if(newUnopenedGiftCount < 0):
            newUnopenedGiftCount = 0
        self.unopenedGiftCount = newUnopenedGiftCount
        
    #reset this counter every round
    #game ends if all players pass in the same round
    def all_passed_end(self) -> bool:
        if self.passCount >= self.playerCount:
            return True
        return False
    
    #game ends if all but 1 player is locked and there are no gifts to open
    def players_locked_end(self) -> bool:
        if self.unlockedPlayerCount <= 1 and self.unopenedGiftCount == 0:
            return True
        return False
    
    def total_players(self) -> int:
        return self.playerCount
    
    #for list of len > 1 will shuffle until the input doesn't match the output
    def shuffle_players(self) -> None:
        if(len(self.playerList) <= 1):
            return
        old_list = copy.deepcopy(self.playerList)
        while(old_list == self.playerList):
            random.shuffle(self.playerList)
        
    def pass_count_up(self) -> None:
        self.passCount += 1
    
    def pass_count_down(self) -> None:
        self.passCount -= 1
        
    def unlocked_player_count_up(self) -> None:
        self.unlockedPlayerCount += 1
    
    def unlocked_player_count_down(self) -> None:
        self.unlockedPlayerCount -= 1
    
    def unopened_gift_count_up(self) -> None:
        self.unopenedGiftCount += 1
    
    def unopened_gift_count_down(self) -> None:
        self.unopenedGiftCount -= 1