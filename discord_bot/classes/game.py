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
    
    def get_current_player_index(self) -> int:
        return self.currentPlayerIndex
    
    def set_current_player_index(self,newIndex: int) -> None:
        self.currentPlayerIndex = newIndex
    
    def get_pass_count(self) -> int:
        return self.passCount
        
    def set_pass_count(self, newPassCount: int) -> None:
        self.passCount = newPassCount
        
    def get_locked_player_count(self) -> int:
        return self.lockedPlayerCount
    
    def set_locked_player_count(self, newLockedPlayerCount: int) -> int:
        self.lockedPlayerCount = newLockedPlayerCount
        
    def too_many_passes(self) -> bool:
        if self.passCount >= self.playerCount:
            return True
        return False
    
    def all_players_locked(self) -> bool:
        if self.lockedPlayerCount >= self.playerCount:
            return True
        return False