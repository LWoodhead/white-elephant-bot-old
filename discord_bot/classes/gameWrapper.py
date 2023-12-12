from .player import Player
from .template import Template
from .game import Game as game

class GameWrapper():
    
    def __init__(self, gameId: int, config: Template, playerList: [Player]) -> None:
        
        self.gameObject = game.Game(gameId, Template, playerList) 

#Should take in all values required to create a game
#Then creates a game
#Should take game actions: open, pass, steal, shuffle
#Should use turn function
#Should check for game ending
#Should allow for undo action stack of action records
#Needs to check for pass end before rounds shuffle