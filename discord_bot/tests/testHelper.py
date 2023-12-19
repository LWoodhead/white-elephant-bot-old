from classes import gift
from classes import player
from classes import template
from classes import game

class TestHelper:
    
    def __init__(self) -> None:
        pass
    
    
    def create_player_list(players: int) -> [player.Player]:
        playerList = list()

        for id in range(5):
            testGift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
            testPlayer = player.Player(id,"Player-" + str(id),testGift)
            playerList.append(testPlayer)
            
        return playerList
    
    def create_game(gameId: int, players: int, config: template.Template):
        if(config == None):
            config = TestHelper.default_config()
        playerList = TestHelper.create_player_list()
        newGame = game.Game(0,config,playerList)
        
        return newGame
    
    def default_config() -> template.Template:
        config = template.Template(False,False,False,3)
        return config