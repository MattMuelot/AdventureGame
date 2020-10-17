import random
from items_weapons import *
import time
from rooms import Room


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


# player = Player(input('Hello! What is your name?: ').title())
# while True:
#     option = input('Check (R)oom | Check (I)tems | Check (W)eapons | (E)quip Weapon | >: ').upper()
#     if option == 'R':
#         r = Room()
#         if r.enemy is None:
#             print('No enemies! Now lets check for loot')
