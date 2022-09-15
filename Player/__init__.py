from uuid import uuid1

import Game
from vec import vec
import World


class Player:
    def __init__(self):
        self.number=None
        self.game:Game.Game
        self.pose=vec()
        self.world:World.World