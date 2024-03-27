from classes import gift

gift_a = gift.Gift(0,"Gark","www.game.com","garf.png")
gift_b = gift.Gift(1,"Game",None,"game.png")
    
def test_gift():
    assert gift_a.id == 0
    assert gift_a.title == "Gark"
    assert gift_a.link == "www.game.com"
    assert gift_a.stolenCount == 0
    assert gift_a.isWrapped is True
    assert gift_b.id == 1
    assert gift_b.title == "Game"
    assert gift_b.link is None
    
def test_get_id():
    assert gift_a.get_id() == 0
        
def test_open():
    gift_a.isWrapped = True
    gift_a.open()
    assert gift_a.isWrapped is False
    
def test_close():
    gift_a.isWrapped = False
    gift_a.close()
    assert gift_a.isWrapped is True
    
def test_steal():
    gift_a.stolenCount = 0
    gift_a.steal()
    assert gift_a.stolenCount == 1
    
def test_release():
    gift_a.stolenCount = 3
    gift_a.release()
    assert gift_a.stolenCount == 2
    
def test_set_title():
    gift_a.set_title("Dead Space")
    assert gift_a.title == "Dead Space"
    gift_a.title = "Gark"
    
def test_get_title():
    gift_a.title = "Gark"
    assert gift_a.get_title() == "Gark"
    
def test_set_link():
    gift_a.set_link("www.steam.com/csgo2")
    assert gift_a.link == "www.steam.com/csgo2"
    gift_a.link = "www.game.com"
    
def test_get_link():
    gift_a.link = "www.game.com"
    assert gift_a.get_link() == "www.game.com"
    
def test_set_wrapping():
    gift_a.set_wrapping("new image.png")
    assert gift_a.wrapping == "new image.png"
    gift_a.wrapping = "garf.png"
    
def test_get_wrapping():
    gift_a.wrapping = "garf.png"
    assert gift_a.get_wrapping() == "garf.png"
    
def test_get_stolen_count():
    gift_a.stolenCount = 2
    assert gift_a.get_stolen_count() == 2
    
def test_set_stolen_count():
    gift_a.set_stolen_count(3)
    assert gift_a.stolenCount == 3
    gift_a.set_stolen_count(-1)
    assert gift_a.stolenCount == 0
    
def test_get_is_wrapped():
    assert gift_a.get_is_wrapped() == gift_a.isWrapped