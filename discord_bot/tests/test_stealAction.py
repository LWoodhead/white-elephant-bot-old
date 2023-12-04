from classes import gift
from classes import player
from classes import template
from classes import game
from classes import stealAction

test_player_list = list()

#list size must be > 2
for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)

stealAction_test = stealAction.StealAction()

def test_steal():
    assert stealAction_test == stealAction_test
    
def test_do():
    #Test one gift as none
    target_gift = test_player_list[0].originalGift
    target_steal_count = test_player_list[0].originalGift.stolenCount
    test_player_list[0].gameGift = None
    test_player_list[1].gameGift = test_player_list[0].originalGift
    stealAction_test.do(game_a,0,test_player_list[0],test_player_list[1])
    assert test_player_list[0].gameGift == target_gift
    assert test_player_list[1].gameGift == None
    assert test_player_list[0].gameGift.stolenCount  == target_steal_count + 1
    
    #Test both gifts as not none 
    target_gift_1 = test_player_list[0].originalGift
    target_gift_2 = test_player_list[1].originalGift
    test_player_list[0].gameGift = test_player_list[1].originalGift
    test_player_list[1].gameGift = test_player_list[0].originalGift
    target_steal_count_1 = test_player_list[0].originalGift.stolenCount
    target_steal_count_2 = test_player_list[1].originalGift.stolenCount
    stealAction_test.do(game_a,1,test_player_list[0],test_player_list[1])
    assert test_player_list[0].gameGift == target_gift_1
    assert test_player_list[1].gameGift == target_gift_2
    assert test_player_list[0].gameGift.stolenCount == target_steal_count_1 + 1
    assert test_player_list[1].gameGift.stolenCount == target_steal_count_2

def test_undo():
    target_gift_1 = test_player_list[0].originalGift
    target_gift_2 = test_player_list[1].originalGift
    test_player_list[0].gameGift = test_player_list[1].originalGift
    test_player_list[1].gameGift = test_player_list[0].originalGift
    target_steal_count_1 = test_player_list[0].originalGift.stolenCount
    target_steal_count_2 = test_player_list[1].originalGift.stolenCount
    steal_record = stealAction_test.do(game_a,2,test_player_list[0],test_player_list[1])
    assert test_player_list[0].gameGift.stolenCount  == target_steal_count_1 + 1
    assert test_player_list[1].gameGift.stolenCount  == target_steal_count_2
    stealAction_test.undo(game_a,steal_record)
    assert test_player_list[0].gameGift == target_gift_2
    assert test_player_list[1].gameGift == target_gift_1
    assert test_player_list[0].gameGift.stolenCount == target_steal_count_2
    assert test_player_list[1].gameGift.stolenCount == target_steal_count_1