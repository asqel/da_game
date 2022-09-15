import Entity
import Player
import Textures
import World



def findNumber(d:dict)->int:
    """
    return smallest number for player
    """
    if d=={int:Player.Player}:
        return 0
    k=d.keys()
    for i in range(0,max(k)):
        if i not in k:
            return(i)
    return(max(k)+1)
class Game:
    def __init__(self)->None:
        """
        Create a new game with a default world called prarie
        """
        self.worlds={str:World.World}
        self.players={int:Player.Player}
        self.worlds["prairie"]=World.World(name="prairie")
        
    def addPlayer(self,x:Player.Player)->None:
        """
        add a new player to the game if the number of the player
        isn't specifier then it will be added
        and if the number is already taken a new one will be assigned
        and if the world is not specified then the default one will be assigned
        """
        if isinstance(x,Player.Player):
            if x.number==None or x.number in self.players.keys():
                x.number=findNumber(self.players)
            x.game=self
            self.players[x.number]=x
        else:
            raise Exception("argument for game.add is invalid only argument of type Player is accepted")
    def getPlayer(self,number:int)->Player.Player:
        """
        return the player with the corresponding number
        """
        return(self.players[number])
    def getPlayers(self)->dict:
        """
        return dictionnary of all the player in the game
        dict={int:Player}
        """
        return self.players
    def getWorlds(self)->dict:
        """
        return dictionnary of all the worlds in the game
        dict={str:Worlds}
        """
        return self.worlds
    def getWorld(self,name)->World.World:
        return self.worlds[name]
        
    def loadContent(self,p:Player.Player):
        p.world