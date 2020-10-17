import random
from player_and_inv import Inv


class Enemy:
    def __init__(self):
        self.hp = 3
        self.xp = 3
        self.attack = 3
        self.inventory = Inv()