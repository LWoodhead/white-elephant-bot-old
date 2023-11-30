from abc import ABC, abstractmethod

class Action(ABC):
    
    #Method to perform the action given the correct input
    @abstractmethod
    def do():
        pass
    
    #Method to undo the action given the correct input
    @abstractmethod
    def undo():
        pass