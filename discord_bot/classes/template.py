#All config values should have a default
class Template:
    def __init__(self, finalSteal: bool, supriseGame: bool, 
                 randomizeRoundOrder: bool, maxSteals: int) -> None:
        if finalSteal is None:
            finalSteal = False
        if supriseGame is None:
            supriseGame = False
        if randomizeRoundOrder is None:
            randomizeRoundOrder = False
        if maxSteals is None:
            maxSteals = 3
            
        self.finalSteal = finalSteal
        self.supriseGame = supriseGame
        self.randomizeRoundOrder = randomizeRoundOrder
        self.maxSteals = maxSteals
        
    def get_final_steal(self) -> bool:
        
    def set_final_steal(self, a: bool) -> None:
        
    def get_suprise_game(self) -> bool:
        
    def set_suprise_game(self, a: bool) -> None:
        
    def get_randomize_round_order(self) -> bool:
        
    def set_randomize_round_order(self, a: bool) -> None:
        
    def get_max_steals(self) -> int:
        
    def set_max_steals(self, a: int) -> None: