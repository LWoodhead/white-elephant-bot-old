from classes import gift

gift_a = gift.Gift(0,"Gark","www.game.com")
gift_b = gift.Gift(1,None,None)
    
def test_gift():
    assert gift_a.id == 0
    assert gift_a.title == "Gark"
    assert gift_a.link == "www.game.com"
    assert gift_a.stolenCount == 0
    assert gift_a.isWrapped == True
    assert gift_b.id == 1
    assert gift_b.title == "Default"
    assert gift_b.link == None
    
def test_open():
    gift_a.isWrapped = True
    gift_a.open()
    assert gift_a.isWrapped == False
    
def test_close():
    gift_a.isWrapped = False
    gift_a.close()
    assert gift_a.isWrapped == True
    
def test_steal():
    gift_a.stolenCount = 0
    gift_a.steal()
    assert gift_a.stolenCount == 1
    
def test_release():
    gift_a.stolenCount = 3
    gift_a.release()
    assert gift_a.stolenCount == 2