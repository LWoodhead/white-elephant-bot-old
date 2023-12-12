from classes import gift
from classes import player
from classes import template
from classes import game
from classes import openAction

test_player_list = list()

#list size must be > 2
for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)

openAction_test = openAction.OpenAction()

def test_open():
    assert openAction_test == openAction_test
    
def test_do():
    previous_unopened_count = game_a.get_unopened_gift_count()
    test_opener = test_player_list[0]
    test_target = test_player_list[1]
    target_gift = test_player_list[1].originalGift
    test_player_list[0].gameGift = None
    assert target_gift.isWrapped == True
    openAction_test.do(game_a,0,test_opener,test_target)
    assert test_opener.gameGift == target_gift
    assert test_opener.gameGift.isWrapped == False
    assert game_a.unopenedGiftCount == previous_unopened_count - 1

def test_undo():
    previous_unopened_count = game_a.get_unopened_gift_count()
    test_opener = test_player_list[0]
    test_target = test_player_list[1]
    target_gift = test_player_list[1].originalGift
    test_player_list[0].gameGift = None
    target_gift.isWrapped = True
    open_record = openAction_test.do(game_a,1,test_opener,test_target)
    assert test_opener.gameGift == target_gift
    assert test_opener.gameGift.isWrapped == False
    assert game_a.unopenedGiftCount == previous_unopened_count - 1
    openAction_test.undo(game_a,open_record)
    assert test_opener.gameGift == None
    assert test_target.originalGift.isWrapped == True
    assert game_a.unopenedGiftCount == previous_unopened_count
    
def test_index():
    previous = game_a.currentPlayerIndex
    test_opener = test_player_list[0]
    test_target = test_player_list[1]
    open_record = openAction_test.do(game_a,0,test_opener,test_target)
    assert game_a.currentPlayerIndex == previous + 1
    openAction_test.undo(game_a,open_record)
    assert game_a.currentPlayerIndex == previous