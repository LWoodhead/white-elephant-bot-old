from .gift import Gift
#gameGift is none until game begins
#add locked value to player rather than gift 
class Player:
    def __init__(self, id: int, name: str, 
                 originalGift: Gift) -> None:
        self.id = id
        self.name = name
        self.originalGift = originalGift
        self.gameGift = None
        self.locked = False
    
    def __str__(self) -> str:
        return "(id: %s, name: %s, orignal gift: %s, game gift: %s, locked: %r)" %(self.id, self.name, print(self.gameGift), print(self.originalGift), self.locked)
    
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
        
    def get_locked(self) -> bool:
        return self.locked
        
    def set_locked(self, a: bool) -> None:
         self.locked = a
         
    def is_locked(self) -> bool:
        return self.locked