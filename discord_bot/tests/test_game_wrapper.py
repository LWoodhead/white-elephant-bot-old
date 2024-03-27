from classes import template
from classes import gameWrapper
import copy

from .testHelper import TestHelper

def test_game_wrapepr():
    test_config = TestHelper.default_config()
    assert test_config.maxSteals == 3
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    assert test_wrapper.gameObject.get_player_list() == test_player_list
    assert test_wrapper.gameObject.get_config() == test_config

def test_player_passes():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    previous_pass_count = test_wrapper.gameObject.passCount
    
    test_wrapper.player_passes()
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index + 1
    assert test_wrapper.gameObject.passCount == previous_pass_count + 1
    
def test_player_opens():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    previous_unopened_gift_count = test_wrapper.gameObject.unopenedGiftCount
    target_player = test_player_list[1]
    acting_player = test_player_list[0]
    
    test_wrapper.player_opens(acting_player,target_player)
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index + 1
    assert test_wrapper.gameObject.unopenedGiftCount == previous_unopened_gift_count - 1
    assert acting_player.gameGift == target_player.originalGift
    assert target_player.originalGift.isWrapped is False
    

def test_player_steals():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    target_player = test_player_list[1]
    acting_player = test_player_list[0]
    target_player.gameGift = test_player_list[2].originalGift
    acting_player.gameGift = test_player_list[3].originalGift
    target_gift = test_player_list[2].originalGift
    acting_gift = test_player_list[3].originalGift
    previous_locked_count = test_wrapper.gameObject.unlockedPlayerCount
    previous_steal_count = target_gift.stolenCount
    
    test_wrapper.player_steals(acting_player,target_player)
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index + 1
    assert acting_player.gameGift == target_gift
    assert target_player.gameGift == acting_gift
    assert test_wrapper.gameObject.unlockedPlayerCount == previous_locked_count
    assert target_gift.stolenCount == previous_steal_count + 1
    
    
def test_is_game_over():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    
    #Not over
    assert test_wrapper.is_game_over() is False
    
    #Pass end
    test_wrapper.gameObject.passCount = test_wrapper.gameObject.playerCount
    assert test_wrapper.is_game_over() is True
    test_wrapper.gameObject.passCount = 0
    
    #Locked end
    test_wrapper.gameObject.unlockedPlayerCount = 1
    test_wrapper.gameObject.unopenedGiftCount = 0
    assert test_wrapper.is_game_over() is True
    test_wrapper.gameObject.unlockedPlayerCount = test_wrapper.gameObject.playerCount
    test_wrapper.gameObject.unopenedGiftCount = test_wrapper.gameObject.playerCount
    
    #Both
    test_wrapper.gameObject.passCount = test_wrapper.gameObject.playerCount
    test_wrapper.gameObject.unlockedPlayerCount = 1
    test_wrapper.gameObject.unopenedGiftCount = 0
    assert test_wrapper.is_game_over() is True

def test_new_round_no_shuffle():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    previous_player_list = copy.deepcopy(test_player_list)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    
    previous_action_count = test_wrapper.actionCounter
    previous_stack_size = len(test_wrapper.actionStack)
    
    test_wrapper.new_round()
    assert test_wrapper.gameObject.currentPlayerIndex == 0
    assert test_wrapper.gameObject.passCount == 0
    assert test_wrapper.actionCounter == previous_action_count + 1
    assert len(test_wrapper.actionStack) == previous_stack_size + 1
    assert test_wrapper.actionStack.pop().data['type'] == "noShuffle"
    assert test_wrapper.gameObject.playerList == previous_player_list
    
def test_new_round_with_shuffle():
    test_config_random = template.Template(False,False,True,3)
    test_player_list_random = TestHelper.create_player_list(4)
    previous_player_list_random = copy.deepcopy(test_player_list_random)
    test_wrapper_random = gameWrapper.GameWrapper(1,test_config_random,test_player_list_random)
    previous_action_count_random = test_wrapper_random.actionCounter
    previous_stack_size_random = len(test_wrapper_random.actionStack)
    
    test_wrapper_random.new_round()
    assert test_wrapper_random.gameObject.currentPlayerIndex == 0
    assert test_wrapper_random.gameObject.passCount == 0
    assert test_wrapper_random.actionCounter == previous_action_count_random + 1
    assert len(test_wrapper_random.actionStack) == previous_stack_size_random + 1
    assert test_wrapper_random.actionStack.pop().data['type'] == "shuffle"
    assert test_wrapper_random.gameObject.playerList != previous_player_list_random

def test_pre_pass_end_check():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    
    assert test_wrapper.pre_pass_end_check() is False
    test_wrapper.gameObject.passCount = test_wrapper.gameObject.playerCount - 1
    assert test_wrapper.pre_pass_end_check() is True

def test_undo_last_action_pass():
    #Undo pass
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    previous_pass_count = test_wrapper.gameObject.passCount
    previous_stack_size = len(test_wrapper.actionStack)
    
    test_wrapper.player_passes()
    test_wrapper.undo_last_action()
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index
    assert test_wrapper.gameObject.passCount == previous_pass_count
    assert len(test_wrapper.actionStack) == previous_stack_size
    
    #TODO undo open
    #TODO undo pass/steal/open with a round change after
    
def test_undo_last_action_steal():
    #TODO undo steal
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    target_player = test_player_list[1]
    acting_player = test_player_list[0]
    target_player.gameGift = test_player_list[2].originalGift
    acting_player.gameGift = test_player_list[3].originalGift
    target_gift = test_player_list[2].originalGift
    acting_gift = test_player_list[3].originalGift
    previous_locked_count = test_wrapper.gameObject.unlockedPlayerCount
    previous_steal_count = target_gift.stolenCount
    
    test_wrapper.player_steals(acting_player,target_player)
    assert test_wrapper.gameObject.unlockedPlayerCount == previous_locked_count
    test_wrapper.undo_last_action()
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index
    assert acting_player.gameGift == acting_gift
    assert target_player.gameGift == target_gift
    assert target_gift.stolenCount == previous_steal_count
    assert test_wrapper.gameObject.unlockedPlayerCount == previous_locked_count
    
def test_undo_last_action_open():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    previous_index = test_wrapper.gameObject.currentPlayerIndex
    previous_unopened_gift_count = test_wrapper.gameObject.unopenedGiftCount
    target_player = test_player_list[1]
    acting_player = test_player_list[0]
    
    test_wrapper.player_opens(acting_player,target_player)
    test_wrapper.undo_last_action()
    assert test_wrapper.gameObject.currentPlayerIndex == previous_index
    assert test_wrapper.gameObject.unopenedGiftCount == previous_unopened_gift_count
    assert acting_player.gameGift is None
    assert target_player.originalGift.isWrapped is True
    
def test_undo_last_action_round_change_shuffle():
    test_config_random = template.Template(False,False,True,3)
    test_player_list_random = TestHelper.create_player_list(4)
    previous_player_list_random = copy.deepcopy(test_player_list_random)
    test_wrapper_random = gameWrapper.GameWrapper(1,test_config_random,test_player_list_random)
    test_wrapper_random.player_passes()
    test_wrapper_random.player_passes()
    previous_action_count_random = test_wrapper_random.actionCounter
    previous_stack_size_random = len(test_wrapper_random.actionStack)
    previous_player_index_random = test_wrapper_random.gameObject.currentPlayerIndex
    previous_pass_count_random = test_wrapper_random.gameObject.passCount
    
    previous_unopened_gift_count_random = test_wrapper_random.gameObject.unopenedGiftCount
    target_player = test_player_list_random[1]
    acting_player = test_player_list_random[0]
    
    assert test_wrapper_random.gameObject.playerList == previous_player_list_random
    test_wrapper_random.player_opens(acting_player,target_player)
    test_wrapper_random.new_round()
    test_wrapper_random.undo_last_action()
    #Check to see the open action has been undone
    assert test_wrapper_random.gameObject.currentPlayerIndex == previous_player_index_random
    assert test_wrapper_random.gameObject.unopenedGiftCount == previous_unopened_gift_count_random
    assert acting_player.gameGift is None
    assert target_player.originalGift.isWrapped is True
    #Check to see the round change has been undone
    assert test_wrapper_random.gameObject.passCount == previous_pass_count_random
    assert test_wrapper_random.actionCounter == previous_action_count_random + 2
    assert len(test_wrapper_random.actionStack) == previous_stack_size_random
    assert test_wrapper_random.gameObject.playerList == previous_player_list_random
    
def test_undo_last_action_round_change_no_shuffle():
    # TODO Test undo with an open action that is immediatly followed by a no shuffle round change
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    previous_player_list = copy.deepcopy(test_player_list)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    
    test_wrapper.player_passes()
    test_wrapper.player_passes()
    previous_unopened_gift_count = test_wrapper.gameObject.unopenedGiftCount
    previous_pass_count = test_wrapper.gameObject.passCount
    previous_player_index = test_wrapper.gameObject.currentPlayerIndex
    previous_action_count = test_wrapper.actionCounter
    previous_stack_size = len(test_wrapper.actionStack)
    target_player = test_player_list[1]
    acting_player = test_player_list[0]
    
    assert test_wrapper.gameObject.playerList == previous_player_list
    
    test_wrapper.player_opens(acting_player,target_player)
    test_wrapper.new_round()
    test_wrapper.undo_last_action()
    
    assert test_wrapper.gameObject.currentPlayerIndex == previous_player_index
    assert test_wrapper.gameObject.passCount == previous_pass_count
    assert test_wrapper.actionCounter == previous_action_count + 2
    assert len(test_wrapper.actionStack) == previous_stack_size
    assert test_wrapper.gameObject.unopenedGiftCount == previous_unopened_gift_count
    assert test_wrapper.gameObject.playerList == previous_player_list

def test_currentPlayer():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    assert test_wrapper.gameObject.playerList[test_wrapper.gameObject.currentPlayerIndex] == test_player_list[0]
    
def test_is_locked():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    #Check player is unlocked
    assert test_wrapper.gameObject.playerList[test_wrapper.gameObject.currentPlayerIndex].locked == test_wrapper.current_player_is_locked()
    #Check player is locked
    test_wrapper.gameObject.playerList[test_wrapper.gameObject.currentPlayerIndex].locked = True
    assert test_wrapper.gameObject.playerList[test_wrapper.gameObject.currentPlayerIndex].locked == test_wrapper.current_player_is_locked()

def test_valid_pass():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    #Invalid due to no gift
    assert test_wrapper.valid_pass() is False
    #Valid due to non None gift
    test_wrapper.gameObject.playerList[0].gameGift = test_wrapper.gameObject.playerList[1].originalGift
    assert test_wrapper.valid_pass() is True
    

def test_valid_open():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    #Valid, None game gift
    assert test_wrapper.valid_open() is True
    #Invalid, non None gift
    test_wrapper.gameObject.playerList[0].gameGift = test_wrapper.gameObject.playerList[1].originalGift
    assert test_wrapper.valid_open() is False

def test_valid_stea():
    test_config = TestHelper.default_config()
    test_player_list = TestHelper.create_player_list(4)
    test_wrapper = gameWrapper.GameWrapper(0,test_config,test_player_list)
    #Invalid, no gift to steal
    assert test_wrapper.valid_steal() is False
    #Valid, gift to steal
    test_wrapper.gameObject.playerList[1].gameGift = test_wrapper.gameObject.playerList[0].originalGift
    assert test_wrapper.valid_steal() is True
    #Invalid, player locked
    test_wrapper.gameObject.playerList[1].locked = True
    assert test_wrapper.valid_steal() is False

def test_list_valid_actions():
    pass