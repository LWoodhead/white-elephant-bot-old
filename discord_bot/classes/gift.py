class Gift:
    #title has a default value
    #link has no default and can be None 
    def __init__(self, id: int, title: str, link: str) -> None:
        self.id = id
        if title is None:
            title = "Default"
        self.link = link
        self.title = title
        self.isWrapped = True
        self.stolenCount = 0
        
    def __str__(self) -> str:
        return "(id: %s, title: %s, isWrapped: %r)" %(self.id, self.title, self.isWrapped)
    
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