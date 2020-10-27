import random
from items_weapons import Item, Weapon
from player_and_inv import Enemy


class CreateRoom:
    def __init__(self):
        self.room_type = random.choice(['enemy', 'empty', 'loot'])
        self.loot = []
        self.enemy = None

    def load_room(self):
        if self.room_type == 'loot':
            num_of_items = random.randint(1, 3)
            for _ in range(num_of_items):
                self.loot.append(Item())
        elif self.room_type == 'enemy':
            pass


r = CreateRoom()
