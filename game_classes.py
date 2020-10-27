import random


class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inv()
        self.hp = 7
        self.max_hp = 10
        self.equipped = None

    def use_item(self, item):
        for i in self.inventory.items:
            if item.name == i.name:
                choice = input(f'{i.name} - HP: {i.hp} | Use Item? Y/N: ').upper()
                if choice == 'Y':
                    if self.hp + i.hp <= self.max_hp:
                        self.hp += i.hp
                    else:
                        print('Failure - HP ERROR')
                elif choice == 'N':
                    continue


class Enemy:
    def __init__(self):
        self.hp = 3
        self.xp = 3
        self.attack = 3
        self.inventory = Inv()


class Inv:
    def __init__(self):
        self.items = []
        self.max_items = 5

    def add_item(self, item):
        if len(self.items) < self.max_items:
            self.items.append(item)
        else:
            choice = input('Inventory Full - Make Room? Y/N: ').upper()
            if choice == 'Y':
                self.drop_item()
            else:
                print(f'Dropping {item.name}')

    def drop_item(self):
        for i in self.items:
            choice = input(f'{i.name} - HP: {i.hp}')


class Room:
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


class Item:
    def __init__(self):
        self.name = random.choice(['Healing Potion', 'Bread', 'Apple', 'Beer'])
        if self.name == 'Apple':
            self.hp = 3
        elif self.name == 'Bread':
            self.hp = 5
        elif self.name == 'Healing Potion':
            self.hp = 100
        elif self.name == 'Beer':
            self.hp = 7


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
