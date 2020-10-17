import random
from items import *


class Room:
    def __init__(self):
        self.room_type = random.choice(['enemy', 'empty', 'loot'])
        self.loot = []

    def load_room(self):
        if self.room_type == 'loot':
            num_of_items = random.randint(1, 3)
            for _ in range(num_of_items):
                self.loot.append(Item())


r = Room()
r.load_room()
for i in r.loot:
    print(i.name)