from .gift import Gift
#gameGift is none until game begins 
class Player:
    def __init__(self, id: int, name: str, 
                 originalGift: Gift) -> None:
        self.id = id
        self.name = name
        self.originalGift = originalGift
        self.gameGift = None
    
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> str:    
        return self.name
        
    def set_name(self, newName: str) -> None:
        self.name = newName
            
    def get_original_gift(self) -> Gift:
        return self.originalGift
    
    def set_original_gift(self, newGift: Gift) -> None:
        self.originalGift = newGift
            
    def get_game_gift(self) -> Gift:
        return self.gameGift
    
    def set_game_gift(self, newGift: Gift) -> None:
        self.gameGift = newGift