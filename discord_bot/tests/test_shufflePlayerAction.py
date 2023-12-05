from classes import gift
from classes import player
from classes import template
from classes import game
from classes import shufflePlayersAction
import copy

test_player_list = list()

for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)
shuffleAction = shufflePlayersAction.ShufflePlayersAction()

def test_shuffle():
    assert shuffleAction == shuffleAction
    
def test_do():
    old_list = copy.deepcopy(game_a.playerList)
    assert old_list == game_a.playerList
    shuffleAction.do(game_a,0)
    assert old_list != game_a.playerList
    assert game_a.passCount == 0
    
def test_undo():
    old_pass_count = game_a.get_pass_count()
    test_data = shuffleAction.do(game_a,1)
    shuffleAction.undo(game_a,test_data)
    assert game_a.playerList == test_data.data['prevPlayerList']
    assert game_a.passCount == test_data.data['prevPassCount']
    assert game_a.passCount == old_pass_count