from classes import gift
from classes import player
from classes import template
from classes import game
from classes import passAction

test_player_list = list()

for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)
passAction_a = passAction.PassAction()

def test_pass():
    assert passAction_a == passAction_a
    
def test_do():
    previous = game_a.passCount
    passAction_a.do(game_a,0)
    assert game_a.currentPlayerIndex == 1
    assert game_a.passCount == previous + 1
    passAction_a.do(game_a,1)
    assert game_a.currentPlayerIndex == 2
    assert game_a.passCount == previous + 2
    
    
def test_undo():
    previous = game_a.passCount
    test_data = passAction_a.do(game_a,1)
    assert game_a.passCount == previous + 1
    passAction_a.undo(game_a,test_data)
    assert game_a.currentPlayerIndex == test_data.data['lastPlayerIndex']
    assert game_a.passCount == previous