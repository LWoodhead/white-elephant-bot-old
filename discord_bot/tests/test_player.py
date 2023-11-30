from classes import player
from classes import gift

default_name = "Rile"
gift_a = gift.Gift(0,"Gark","www.game.com","garf.png")
gift_b = gift.Gift(1,"Game",None,"game.png")
player_a = player.Player(0,default_name,gift_a)

def test_player() -> None:
    assert player_a.id == 0
    assert player_a.name == "Rile"
    assert player_a.originalGift == gift_a
    assert player_a.gameGift == None
    
def test_get_id():
    assert player_a.get_id() == player_a.id    
    
def test_get_name():
    assert player_a.get_name() == player_a.name
    
def test_set_name():
    player_a.set_name("Josh")
    assert player_a.get_name() == "Josh"
    player_a.name = default_name
    
def test_get_original_gift():
    assert player_a.originalGift == gift_a
    
def test_set_original_gift():
    player_a.set_original_gift(gift_b)
    assert player_a.originalGift == gift_b
    player_a.originalGift = gift_a
    
def test_get_game_gift():
    assert player_a.get_game_gift() == player_a.gameGift
    
def test_set_game_gift():
    player_a.set_game_gift(gift_b)
    assert player_a.gameGift == gift_b
    player_a.gameGift = gift_a
    
def test_get_locked():
    assert player_a.get_locked() == player_a.locked
    
def test_set_locked():
    player_a.set_locked(True)
    assert player_a.locked == True
    
def test_is_locked():
    assert player_a.is_locked() == player_a.locked