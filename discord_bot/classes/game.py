from .player import Player
from .template import Template
from typing import Final

class Game:
    
    def __init__(self, id: int, config: Template, playerList: [Player]) -> None:
        self.id = id
        self.config = config
        self.playerList = playerList
        self.currentPlayerIndex = 0
        self.passCount = 0
        self.lockedPlayerCount = 0
        self.playerCount: Final = len(self.playerList)
        
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
        
    def get_locked_player_count(self) -> int:
        return self.lockedPlayerCount
    
    def set_locked_player_count(self, newLockedPlayerCount: int) -> int:
        if(newLockedPlayerCount < 0):
            newLockedPlayerCount = 0
        self.lockedPlayerCount = newLockedPlayerCount
    
    #reset this counter every round
    #game ends if all players pass in the same round
    def all_passed_end(self) -> bool:
        if self.passCount >= self.playerCount:
            return True
        return False
    
    #game ends if all but 1 player is locked
    def players_locked_end(self) -> bool:
        if self.lockedPlayerCount >= self.playerCount - 1:
            return True
        return False
    
    def total_players(self):
        return self.playerCount