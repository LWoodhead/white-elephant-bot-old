from classes import template

template_a = template.Template(True,True,False,4)
template_b = template.Template(None,None,None,None)
template_c = template.Template(True,True,True,-4)

def test_template():
    assert template_a.finalSteal is True
    assert template_a.supriseGame is True
    assert template_a.randomizeRoundOrder is False
    assert template_a.maxSteals == 4
    
    assert template_b.finalSteal is False
    assert template_b.supriseGame is False
    assert template_b.randomizeRoundOrder is False
    assert template_b.maxSteals == 3
    
    assert template_c.maxSteals == 3
    
    
def test_get_final_steal():
    assert template_a.get_final_steal() == template_a.finalSteal
        
def test_set_final_steal():
    template_a.set_final_steal(False)
    assert template_a.finalSteal is False
        
def test_get_suprise_game():
    assert template_a.get_suprise_game() == template_a.supriseGame
        
def test_set_suprise_game():
    template_a.set_suprise_game(False)
    assert template_a.supriseGame is False
        
def test_get_randomize_round_order():
    assert template_a.get_randomize_round_order() == template_a.randomizeRoundOrder
        
def test_set_randomize_round_order():
    template_a.set_randomize_round_order(True)
    assert template_a.randomizeRoundOrder is True
        
def test_get_max_steals():
    assert template_a.get_max_steals() == template_a.maxSteals
        
def test_set_max_steals():
    template_a.set_max_steals(7)
    assert template_a.maxSteals == 7