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
    assert game_a.lockedPlayerCount == 0
    assert game_a.playerCount == len(test_player_list)
    
def test_get_id():
    assert game_a.get_id() == game_a.id
        
def test_get_config():
    assert game_a.get_config() == template_a
    
def test_get_player_list():
    assert game_a.get_player_list() == test_player_list
    
def test_set_player_list():
    game_a.set_player_list(test_player_list_2)
    assert game_a.playerList == test_player_list_2
    
def test_get_current_player_index():
    assert game_a.get_current_player_index() == game_a.currentPlayerIndex
    
def test_set_current_player_index():
    game_a.set_current_player_index(4)
    assert game_a.currentPlayerIndex == 4
    game_a.set_current_player_index(12)
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

def test_get_locked_player_count():
    assert game_a.get_locked_player_count() == game_a.lockedPlayerCount

def test_set_locked_player_count():
    game_a.set_locked_player_count(3)
    assert game_a.lockedPlayerCount == 3
    game_a.set_locked_player_count(-1)
    assert game_a.lockedPlayerCount == 0

def test_all_passed_end():
    game_a.passCount = len(test_player_list)
    assert game_a.all_passed_end() == True
    game_a.passCount = len(test_player_list) - 1
    assert game_a.all_passed_end() == False

def test_players_locked_end():
    game_a.lockedPlayerCount = len(test_player_list) - 1
    assert game_a.players_locked_end() == True
    game_a.lockedPlayerCount = len(test_player_list) - 2
    assert game_a.players_locked_end() == False
    
def test_total_players():
    assert game_a.total_players() == len(test_player_list)
    
def test_shuffle_players():
    old_list = copy.deepcopy(game_a.playerList)
    game_a.shuffle_players()
    assert old_list != game_a.playerList