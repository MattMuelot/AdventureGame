import random


class Item:
    def __init__(self):
        self.name = random.choice(['Healing Potion', 'Bread', 'Apple', 'Beer'])
        if self.name == 'Apple':
            self.hp = 3
            self.xp = 0
        elif self.name == 'Bread':
            self.hp = 5
            self.xp = 0
        elif self.name == 'Healing Potion':
            self.hp = 100
            self.xp = 0
        elif self.name == 'Beer':
            self.hp = 7
            self.xp = 0


class Weapon:
    def __init__(self):
        self.name = random.choice('Club', 'Dagger', 'Sword', 'Spear')
        if self.name == 'Club':
            self.damage = 3
        elif self.name == 'Dagger':
            self.damage = 4
        elif self.name == 'Sword':
            self.damage = 5
        elif self.name == 'Spear':
            self.damage = 7
