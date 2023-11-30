class ActionRecord:
    
    #data should be a dict with all relevant state information to undo the action
    #the type field should be the type of action: steal, pass, unwrap, new round, game end, etc 
    def __init__(self, id: int, 
                 data: {"type" : str, 'info': int, "..." : str}) -> None:
        self.id = id
        self.data = data