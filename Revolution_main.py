import sys
import os
import random
import pickle
import math
import time

Weapons = {'Sword': 40,
           'Dagger': 30,
           'Axe': 100,
           'Pickaxe': 150,
           'Knive': 350,
           'Club': 50,
           }

Items = {"Potions": 30
         }

Magic = {"Fireball",
         "Ice Shards",
         "Ghoul"}


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 25
        self.gold = 0
        self.pot = 2
        self.weapon = ["Rusty Sword"]
        self.curweap = ["Rusty Sword"]
        self.lvl = 1
        self.xp = 0
    @property
    def attack(self):
        attack = self.base_attack
        if self.curweap == 'Rusty Sword':
            attack += 5

        if self.curweap == 'Sword':
            attack += 15

        if self.curweap == 'Axe':
            attack += 20

        if self.curweap == "Pickaxe":
            attack += 40

        if self.curweap == "Knive":
            attack += 100
        return attack

class Monster:
    def __init__(self, name, class_, attack, gold, exp):
        self.name = name
        self.class_ = class_
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = attack
        self.goldgain = gold
        self.exp = exp
        # Use the stats property to view all the stats of the Character
        self.stats = [
            self.name,
            self.class_,
            self.maxhealth,
            self.attack,
            self.goldgain,
            self.exp,
        ]

# Enemy Names(add new monster names here)
Beast_names = [
    'Goblin',
    'Skeletons',
    'Dragon',
    'Golem',
    'Wolf'
]

Attr = [
    "Fire",
    "Earth",
    "Magic",
    "Warrior",
]

# Fight System **Work in Progress**
def fight():
    global Monster
    goblin = Monster(Beast_names[0], Attr[3], "30", "50", "5")
    print(goblin.stats)

def start1():
    pass

# First page when player starts the game
def main():
    os.system('cls')
    print("Hello what is your name?")
    option1 = input("> ")
    global PlayerIG
    if len(option1) <= 0:
        os.system('cls')
        print("Please input something.")
        start()
    if option1 == 'frisk':
        print("Do you want to continue with this name?\nYour life will be a living hell!")
        option = input('> ')
        if option == 'yes':
            hard()
        else:
            start()
    else:
        PlayerIG = Player(option1)
        start()


# Leveling system for the game
def uplvl():
    pass

def store():
    print(f"Hello {PlayerIG.name}! Welcome to Gary's  .\nYou currently have {PlayerIG.gold} Gold.")
    print("**********")
    # Shows a list of weapons available
    for weapon in Weapons:
        print(weapon + ":", str(Weapons[weapon])+" Gold")
    print("**********\n")
    option = input("What would you like to buy today?\n> ")
    
        





# Home Page to navigate around everywhere
def start():
    uplvl()
    # Displays the Stats of the Player
    print(
        f"Name: {PlayerIG.name}\nAttack: {PlayerIG.attack}\nCurrent Weapon: {PlayerIG.curweap}\nHealth: {PlayerIG.health}/{PlayerIG.maxhealth}\nGold: {PlayerIG.gold}\nLevel: {PlayerIG.lvl}\nExp: {PlayerIG.xp}"
    )
    decision = input("1. Fight\n2. Store\n3. Save and Quit\n> ")

    if decision == '1':
        fight()
    if decision == '2':
        store()
    if decision == '3':
        save()
    else:
        start()

main()
