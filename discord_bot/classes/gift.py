class Gift:
    #link has no default and can be None
    #wrapping is a filename for wrapping image file 
    def __init__(self, id: int, title: str, link: str, wrapping: str) -> None:
        self.id = id
        self.title = title
        self.link = link
        self.isWrapped = True
        self.wrapping = wrapping
        self.stolenCount = 0
        
    def __str__(self) -> str:
        return "(id: %s, title: %s, isWrapped: %r)" %(self.id, self.title, self.isWrapped)
    
    def __eq__(self, __value: object) -> bool:
        if(__value == None):
            return False
        if(self.id != __value.id):
            return False
        if(self.title != __value.title):
            return False
        if(self.link != __value.link):
            return False
        if(self.isWrapped != __value.isWrapped):
            return False
        if(self.wrapping != __value.wrapping):
            return False
        if(self.stolenCount != __value.stolenCount):
            return False
        return True
    
    def get_id(self) -> int:
        return self.id
    
    def open(self) -> None:
        self.isWrapped = False
        
    def close(self) -> None:
        self.isWrapped = True
        
    def steal(self) -> int:
        self.stolenCount += 1
        return self.stolenCount
    
    def release(self) -> int:
        self.stolenCount -= 1
        return self.stolenCount
    
    def get_title(self) -> str:
        return self.title
    
    def set_title(self, newTitle: str) -> None:
        self.title = newTitle
        
    def get_link(self) -> str:
        return self.link
        
    def set_link(self, newLink: str) -> None:
        self.link = newLink
        
    def get_wrapping(self) -> str:
        return self.wrapping
    
    def set_wrapping(self, newWrapping: str) -> None:
        self.wrapping = newWrapping
    
    def get_stolen_count(self) -> None:
        return self.stolenCount
    
    def set_stolen_count(self, newStolenCount) -> int:
        if(newStolenCount < 0):
            newStolenCount = 0
        self.stolenCount = newStolenCount
        
    def get_is_wrapped(self) -> bool:
        return self.isWrapped