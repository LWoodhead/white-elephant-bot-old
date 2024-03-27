class IdentifierGenerator:
    gameIdentifier = 0
    
    #TODO add functionality to generate a unique game id
    def generateGameIdentifier():
        IdentifierGenerator.gameIdentifier += 1
        return IdentifierGenerator.gameIdentifier