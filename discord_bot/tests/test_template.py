from classes import template

template_a = template.Template(True,True,False,4)
template_b = template.Template(None,None,None,None)

def test_template():
    assert template_a.finalSteal == True
    assert template_a.supriseGame == True
    assert template_a.randomizeRoundOrder == False
    assert template_a.maxSteals == 4
    
    assert template_b.finalSteal == False
    assert template_b.supriseGame == False
    assert template_b.randomizeRoundOrder == False
    assert template_b.maxSteals == 3
    
    
def test_get_final_steal():
    assert template_a.get_final_steal() == template_a.finalSteal
        
def test_set_final_steal():
    template_a.set_final_steal(False)
    assert template_a.finalSteal == False
        
def test_get_suprise_game():
    assert template_a.get_suprise_game() == template_a.supriseGame
        
def test_set_suprise_game():
    template_a.set_suprise_game(False)
    assert template_a.supriseGame == False
        
def test_get_randomize_round_order():
    assert template_a.get_randomize_round_order() == template_a.randomizeRoundOrder
        
def test_set_randomize_round_order():
    template_a.set_randomize_round_order(True)
    assert template_a.randomizeRoundOrder == True
        
def test_get_max_steals():
    assert template_a.get_max_steals() == template_a.maxSteals
        
def test_set_max_steals():
    template_a.set_max_steals(7)
    assert template_a.maxSteals == 7