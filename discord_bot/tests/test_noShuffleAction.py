from classes import gift
from classes import player
from classes import template
from classes import game
from classes import noShuffleAction

test_player_list = list()

for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)
no_shuffle_action = noShuffleAction.NoShuffleAction()

def test_shuffle():
    assert no_shuffle_action == no_shuffle_action
    
def test_do():
    game_a.currentPlayerIndex = game_a.playerCount - 1
    no_shuffle_action.do(game_a,0)
    assert game_a.currentPlayerIndex == 0
    assert game_a.passCount == 0
    
def test_undo():
    game_a.passCount = 3
    old_pass_count = game_a.get_pass_count()
    game_a.currentPlayerIndex = game_a.playerCount - 1
    prev_index = game_a.currentPlayerIndex
    test_data = no_shuffle_action.do(game_a,1)
    assert game_a.currentPlayerIndex != prev_index
    no_shuffle_action.undo(game_a,test_data)
    assert game_a.passCount == test_data.data['prevPassCount']
    assert game_a.passCount == old_pass_count
    assert game_a.currentPlayerIndex == test_data.data['prevIndex']
    assert game_a.currentPlayerIndex == prev_index