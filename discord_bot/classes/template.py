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
        if maxSteals is None or maxSteals < 0:
            maxSteals = 3
            
        self.finalSteal = finalSteal
        self.supriseGame = supriseGame
        self.randomizeRoundOrder = randomizeRoundOrder
        self.maxSteals = maxSteals
        
    def __str__(self) -> str:
        return "(final steal: %r, suprise game: %r, randomize round order: %r, max steals: %d)" %(
            self.finalSteal, self.supriseGame, self.randomizeRoundOrder, self.maxSteals)
        
    def get_final_steal(self) -> bool:
        return self.finalSteal
        
    def set_final_steal(self, a: bool) -> None:
        self.finalSteal = a
        
    def get_suprise_game(self) -> bool:
        return self.supriseGame
        
    def set_suprise_game(self, a: bool) -> None:
        self.supriseGame = a
        
    def get_randomize_round_order(self) -> bool:
        return self.randomizeRoundOrder
        
    def set_randomize_round_order(self, a: bool) -> None:
        self.randomizeRoundOrder = a
        
    def get_max_steals(self) -> int:
        return self.maxSteals
        
    def set_max_steals(self, a: int) -> None:
        self.maxSteals = a