import random


class Item:
    def __init__(self):
        self.item_names = ['Apple', 'Bread', 'Ice Cream', 'Poison Gas']
        self.name = random.choice(self.item_names)
        self.hp = random.randint(1, 4)
