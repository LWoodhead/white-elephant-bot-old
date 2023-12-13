from classes import gift
from classes import player
from classes import template
from classes import game
import copy

test_player_list = list()
test_player_list_2 = list()

for id in range(5):
    test_gift = gift.Gift(id, "Game-" + str(id), "link-" + str(id), "picture-" + str(id) + ".png")
    test_player = player.Player(id,"Player-" + str(id),test_gift)
    test_player_list.append(test_player)
    
test_player_list_2.append(player.Player(6,"Player-6",gift.Gift(6,"Game-6","link-6","picture-6.png")))

template_a = template.Template(True,True,False,4)
game_a = game.Game(0,template_a,test_player_list)

def test_game():
    assert game_a.id == 0
    assert game_a.config == template_a
    assert game_a.playerList == test_player_list
    assert game_a.currentPlayerIndex == 0
    assert game_a.passCount == 0
    assert game_a.unlockedPlayerCount == len(test_player_list)
    assert game_a.playerCount == len(test_player_list)
    assert game_a.unopenedGiftCount == len(test_player_list)
    
def test_get_id():
    assert game_a.get_id() == game_a.id
        
def test_get_config():
    assert game_a.get_config() == template_a
    
def test_get_player_list():
    assert game_a.get_player_list() == test_player_list
    
def test_set_player_list():
    game_a.set_player_list(test_player_list_2)
    assert game_a.playerList == test_player_list_2
    game_a.playerList = test_player_list
    
def test_get_current_player_index():
    assert game_a.get_current_player_index() == game_a.currentPlayerIndex
    
def test_set_current_player_index():
    assert len(test_player_list) == 5
    game_a.playerList = test_player_list
    game_a.set_current_player_index(4)
    assert game_a.currentPlayerIndex == 4
    game_a.set_current_player_index(5)
    assert game_a.currentPlayerIndex == 0
    game_a.set_current_player_index(-4)
    assert game_a.currentPlayerIndex == 0

def test_get_pass_count():
    assert game_a.get_pass_count() == game_a.passCount

def test_set_pass_count():
    game_a.set_pass_count(4)
    assert game_a.passCount == 4
    game_a.set_pass_count(-1)
    assert game_a.passCount == 0

def test_get_plaer_count():
    assert game_a.get_player_count() == game_a.playerCount

def test_get_locked_player_count():
    assert game_a.get_unlocked_player_count() == game_a.unlockedPlayerCount

def test_set_locked_player_count():
    game_a.set_unlocked_player_count(3)
    assert game_a.unlockedPlayerCount == 3
    game_a.set_unlocked_player_count(-1)
    assert game_a.unlockedPlayerCount == 0
    
def test_get_unopened_gift_count():
    assert game_a.get_unopened_gift_count() == game_a.unopenedGiftCount

def test_set_unopened_gift_count():
    game_a.set_unopened_gift_count(3)
    assert game_a.unopenedGiftCount == 3
    game_a.set_unopened_gift_count(-1)
    assert game_a.unopenedGiftCount == 0

def test_all_passed_end():
    game_a.passCount = len(test_player_list)
    assert game_a.all_passed_end() == True
    game_a.passCount = len(test_player_list) - 1
    assert game_a.all_passed_end() == False
    
def test_players_locked_end():
    game_a.unlockedPlayerCount = 5
    assert game_a.players_locked_end() == False
    game_a.unlockedPlayerCount = 1
    game_a.unopenedGiftCount = 2
    assert game_a.players_locked_end() == False
    game_a.unopenedGiftCount = 0
    assert game_a.players_locked_end() == True
    game_a.unlockedPlayerCount = 1
    assert game_a.players_locked_end() == True
    
def test_total_players():
    assert game_a.total_players() == len(test_player_list)
    
def test_shuffle_players():
    old_list = copy.deepcopy(game_a.playerList)
    game_a.shuffle_players()
    assert old_list != game_a.playerList
    
def test_pass_count_up():
    previous = game_a.get_pass_count()
    game_a.pass_count_up()
    assert game_a.get_pass_count() == previous + 1

def test_pass_count_down():
    previous = game_a.get_pass_count()
    game_a.pass_count_down()
    assert game_a.get_pass_count() == previous - 1
    
def test_unlocked_player_count_up() -> None:
    previous = game_a.unlockedPlayerCount
    game_a.unlocked_player_count_up()
    assert game_a.unlockedPlayerCount == previous + 1
    
def test_unlocked_player_count_down() -> None:
    previous = game_a.unlockedPlayerCount
    game_a.unlocked_player_count_down()
    assert game_a.unlockedPlayerCount == previous - 1
    
def test_unopened_gift_count_up() -> None:
    previous = game_a.unopenedGiftCount
    game_a.unopened_gift_count_up()
    assert game_a.unopenedGiftCount == previous + 1
    
def test_unopened_gift_count_down() -> None:
    previous = game_a.unopenedGiftCount
    game_a.unopened_gift_count_down()
    assert game_a.unopenedGiftCount == previous - 1
    
def test_player_index_up():
    game_a.currentPlayerIndex = 0
    game_a.player_index_up()
    assert game_a.currentPlayerIndex == 1
    game_a.currentPlayerIndex = game_a.playerCount
    game_a.player_index_up()
    assert game_a.currentPlayerIndex == 0

def test_player_index_down():
    game_a.currentPlayerIndex = 0
    game_a.player_index_down()
    assert game_a.currentPlayerIndex == game_a.playerCount - 1 
    game_a.currentPlayerIndex = game_a.playerCount
    game_a.player_index_down()
    assert game_a.currentPlayerIndex == game_a.playerCount - 1