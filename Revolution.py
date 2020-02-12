import sys
import os
import random
import pickle
import math
import time



Weapons = {'Sword':40,
           'Dagger':30,
           'Axe':100,
           'Pickaxe':150,
           'Knive':500
           }


Items = {"Potions":30
         }

Magic = {"Fireball",
         "Ice Shards",
         "Ghoul"}

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 100
        self.gold = 500        
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

    
    
class Dog:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 25
        self.attack = 30
        self.goldgain = 5
        self.drop = 1
        self.exp = 2
DogIG = Dog("Dog")

class BoogeyMan:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.attack = 200
        self.goldgain = 200
        self.drop = 0
        self.exp = 250
BoogeyManIG = BoogeyMan("BoogeyMan")

        
class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 10
        self.drop = 1
        self.exp = 10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldgain = 10
        self.drop = 3
        self.exp = 20
ZombieIG = Zombie("Zombie")

class Dragon:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 15
        self.goldgain = 50
        self.drop = 3
        self.exp = 40
DragonIG = Dragon("Dragon")

class Golem:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200
        self.health = self.maxhealth
        self.attack = 20
        self.goldgain = 70
        self.drop = 0
        self.exp = 90
GolemIG = Golem("Golem")

class Troll:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 40
        self.health = self.maxhealth
        self.attack = 30
        self.goldgain = 100
        self.drop = 0
        self.exp = 100
TrollIG = Troll("Troll")

class Wolf:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 20
        self.health = self.maxhealth
        self.attack = 10
        self.goldgain = 10
        self.drop = 3
        self.exp = 10
WolfIG = Wolf("Wolf")

class Phoenix:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 45
        self.goldgain = 100
        self.drop = 0
        self.exp = 60
PhoenixIG = Phoenix("Phoenix")

class Weirdo:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 350
        self.health = self.maxhealth
        self.attack = 50
        self.goldgain = 1000
        self.drop = 0
        self.exp = 100
WeirdoIG = Weirdo("Weirdo")

def main():
    os.system('cls')
    print("Welcome to The Revolution\n")
    print("1. Start")
    print("2. Load")
    print("3. Exit")

    option = input("\n-> ")

    if option == '1':
        start()

    elif option == '2':
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded saved state...")
            option = input(' ')
            start1()
        else:
            print("You have no saved file for this Game.")
            option = input(' ')
            main()
            

    elif option == '3':
        sys.exit()

    elif option == 'dev':
        dev()

    else:
        main()

def start():
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
        start1()

def hard():
    global PlayerIG
    PlayerIG = Player('Frisk')
    PlayerIG.maxhealth = 50
    PlayerIG.health = PlayerIG.maxhealth
    PlayerIG.base_attack = 5
    PlayerIG.pot = 0
    PlayerIG.lvl = -5
    PlayerIG.gold = 50
    
    start1()



def start1():
    os.system('cls')

    uplvl()
    print("Name: %s" % PlayerIG.name)
    print("Attack: %d" % PlayerIG.attack)
    print("Current Weapons: %s" % PlayerIG.curweap)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Gold: %d" % PlayerIG.gold)
    print("Potions: %d" % PlayerIG.pot)
    print("Level: %i" % PlayerIG.lvl)
    print("Experience: %i" % PlayerIG.xp)
    print("\n1. Fight")
    print("2. Store")
    print("3.Inventory")
    print("4. Save")
    print("5. Dungeon")
    print("6. Exit")

    option2 = input("> ")

    if option2 == '1':
        if PlayerIG.name == 'Frisk':
            prefight1()
        else:            
            prefight()
    elif option2 == '2':
        store()
    elif option2 == '3':
        inventory()


    elif option2 == '4':
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been Saved!\n")
        option = input(' ')
        start1()
    elif option2 == '5':
        dungeon()
            
    
    elif option2 == '6':
        sys.exit()
    else:
        start1()

def inventory():
    os.system('cls')
    print("What would you like to do?")
    print("\n1. Equip Weapons")
    print("2. Drink Potions")
    print("\nBack")
    option = input("> ")

    if option == '1':
        equip()

    elif option == '2':
        os.system('cls')
        if PlayerIG.pot == 0:
            print("You don't have any potions left")       
        else:
            PlayerIG.health += 20
            if PlayerIG.health > PlayerIG.maxhealth:
                PlayerIG.health = PlayerIG.maxhealth
            PlayerIG.pot -= 1
            print("You drank a potion")
        option = input(' ')
        inventory()
        
        

    
    elif option == 'back':
        start1()

    else:
        inventory()
def equip():
    os.system('cls')
    print("You are currently equipped with %s." % PlayerIG.curweap)
    print("What do you want to equip?\n")
    for weapon in PlayerIG.weapon:
        print(weapon)
    print("Enter b to go back.")
    option = input("> ")
    if option == PlayerIG.curweap:
        print("You have already equipped that item")
        option = input(' ')
        equip()
    elif option == 'b':
        inventory()
    elif option in PlayerIG.weapon:
        PlayerIG.curweap = option
        print("You have equipped %s." %option)
        option = input(' ')
        equip()
    else:
        print("You do not own %s." % option)
        
        
def dodge():
    maxDodge = []
    n = 5
    while n > 0:
        time.sleep(.3)
        n -= 1
        os.system('cls')
        if n <= 0:
            print('done')
        if input():
            print('yay')
    
       
        
    
    
def prefight1():
       global enemy
       
       enemy = random.choice((BoogeyManIG, GolemIG, WeirdoIG))
       fight()
       
    
    
        
def prefight():
    global enemy

    enemy = random.choice((ZombieIG, GoblinIG, DragonIG))
        
        
    fight()

def fight():
    os.system('cls')
    print("%s  VS  %s" % (PlayerIG.name, enemy.name))
    print("%s's Health: %d/%d" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth))
    print("%s's Health: %i/%i" % (enemy.name, enemy.health, enemy.maxhealth))
    print("Potions: %i\n" % PlayerIG.pot)    
    print("1. Attack")
    print("2. Potion")
    print("3. Run")
    option = input("> ")

    if option == '1':
        dodge()
        attack()
    elif option == '2':
        drinkpot()
    elif option == '3':
        if PlayerIG.name == 'Frisk':
            prefight()
        else:
            
            run()
    else:
        fight()
        
def attack():
    os.system('cls')
    Pattack = random.randint(0, PlayerIG.attack)
    Eattack = random.randint(0, enemy.attack)
    if Pattack == (PlayerIG.attack /2):
        print("You missed!")
    else:
        enemy.health -= Pattack
        print("You dealt %i damage!" % Pattack)    
    option = input(' ')
    if enemy.health <= 0:
        win()
    
    os.system('cls')
    if Eattack == (enemy.attack /2):
        print("The enemy missed!")
    else:
        PlayerIG.health -= Eattack
        print("The enemy dealt %i damage!" % Eattack)
    option = input(' ')
    if PlayerIG.health <= 0:
        die()
    else:
        fight()
        
        
        
def win():    
    os.system('cls')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldgain
    PlayerIG.pot += enemy.drop
    PlayerIG.xp += enemy.exp
    uplvl()
    option = input(' ')
    print("You have Successfully defeated %s!" % enemy.name)
    print("You have found %i gold " % enemy.goldgain)
    print("%s dropped %i potions for you!" % (enemy.name, enemy.drop))
    option = input(' ')
    start1()
        
    

def die():
    os.system('cls')
    PlayerIG.health = PlayerIG.maxhealth
    enemy.health = enemy.maxhealth
    print("You have been Defeated!")
    option = input(' ')
    start1()
        


def drinkpot():
    os.system('cls')
    if PlayerIG.pot == 0:
        print("You don't have any potions left")       
    else:
        PlayerIG.health += 20
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.pot -= 1
        print("You drank a potion")
    option = input(' ')
    fight()
    
        
    

def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have Successfully ran away!")
        option = input(' ')
        start1()
    else:
        print("You failed to get away!")
        option = input(' ')
        os.system('cls')
        Eattack = random.randint(0, enemy.attack)
        if Eattack <= 0:
            print("The enemy missed!")
        else:
            PlayerIG.health -= Eattack
            print("The enemy dealt %i damage!" % Eattack)
        option = input(' ')
        if PlayerIG.health <= 0:
            die()
        else:
            fight()

##Price List:
#           Sword = 40 Goldz
#           Dagger = 30 Golds
#           Axe = 100 Gold
#           Potions = 25 Gold



def store():
    os.system('cls')
    print("Welcome to Gary's Hob!")
    print("You have %i Gold!" % PlayerIG.gold)
    print("\nWhat would you like to buy?\n")
    print("1. Weapons")
    print("2. Potions")
    print("Back")
    option = input("> ")
    if option in '1':
        os.system('cls')
        print("Welcome to the Weaponary!")
        print("You currently have %i Gold." % PlayerIG.gold)
        print("What would you like to buy?\n")
        print("1. Sword (40 Gold)")
        print("2. Dagger (30 Gold)")
        print("3. Axe (100 Gold)")
        print("4. Knive (500 Gold)")
        print("Back")
        option = input("> ")
        if option in Weapons:
            if PlayerIG.gold >= Weapons[option]:
                os.system('cls')
                PlayerIG.gold -= Weapons[option]
                PlayerIG.weapon.append(option)
                print("You have Successfully purchased %s" % option)
                option = input(' ')
                store()

            else:
                os.system('cls')
                print("You don't have enough Gold!")
                option = input(' ')
                store()
    
        elif option == 'back':
            os.system('cls')
            print("Thank you!")
            option = input(' ')
            os.system('cls')
            store()

        else:
            os.system('cls')
            print("This item does not Exist!")
            option = input(' ')
            store()
    elif option in '2':
        os.system('cls')
        print("Welcome to Items Shop")
        print("What would you like to buy? \n")
        print("1. Potions (30 Gold)")
        print("back")
        option = input("> ")
        if option in Items:
            if PlayerIG.gold >= Items[option]:
                os.system('cls')
                PlayerIG.gold -= Items[option]
                PlayerIG.pot += 1
                
                print("You have successfully purchased %s" % option)
                option = input(' ')
                store()
                
            else:
                os.system('cls')
                print("You don't have enough Gold!")
                option = input(' ')
                store()
        elif option == 'back':
            os.system('cls')
            print("Thank you!")
            option = input(' ')
            os.system('cls')
        else:
            os.system('cls')
            print("This item does not Exist!")
            option = input(' ')
            store()
            
            
    elif option == 'back':
        os.system('cls')
        print("Thank You for Shopping with us!")
        option = input(' ')
        os.system('cls')
        start1()


    else:
        
        return store()
        
            
        


    


def stats():
    os.system('cls')
    print("Current saved progress:")
    print("Name: %s" % PlayerIG.name)
    print("Attack: %d" % PlayerIG.attack)
    print("Current Weapons: %s" % PlayerIG.curweap)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Gold: %d" % PlayerIG.gold)
    print("Potions: %d\n" % PlayerIG.pot)




def dev():
    os.system('cls')
    if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded saved state...")
            option = input(' ')
            stats()
            print("Press Enter to Exit.")
            option = input(' ')
            os.system('cls')
            main()
    else:
        os.system('cls')
        print("There is no saved file please create a new one.")
        print("Press Enter to exit.")
        option = input(' ')
        os.system('cls')
        main()
        
            
def dungeon():
    os.system('cls')
    print("Welcome to Dungeon mode!")
    option = input(' ')
    os.system('cls')
    print("Be prepared to DIE!")
    option = input(' ')
    os.system('cls')
    print("Choose your Mode!")
    print("1. ICE")
    print("2. FIRE")
    print("3. EARTH")
    print("4. back")
    option = input("> ")

    if option == '1':
        ice()
    elif option == '2':
        fire()
    elif option == '3':
        earth()
    elif option == 'back':
        start1()
    else:
        print("That's not a choice!")
        dungeon()


def ifight():
    global enemy

    enemy = random.choice((TrollIG, WolfIG, BoogeyManIG))        
    dunfight()

def ffight():
    global enemy

    enemy = random.choice((PhoenixIG, DragonIG, BoogeyManIG))        
    dunfight()

def efight():
    global enemy

    enemy = random.choice((GolemIG,BoogeyManIG, DogIG))        
    dunfight()





def dunfight():
    os.system('cls')
    print("%s  VS  %s" % (PlayerIG.name, enemy.name))
    print("%s's Health: %d/%d" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth))
    print("%s's Health: %i/%i" % (enemy.name, enemy.health, enemy.maxhealth))
    print("Potions: %i\n" % PlayerIG.pot)    
    print("1. Attack")
    print("2. Potion")
    print("3. Run")
    option = input("> ")

    if option == '1':
        attack()
    elif option == '2':
        drinkpot()
    elif option == '3':
        run1()
    else:
        fight()

def run1():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have Successfully ran away!")
        option = input(' ')
        dungeon()
    else:
        print("You failed to get away!")
        option = input(' ')
        os.system('cls')
        Eattack = random.randint(0, enemy.attack)
        if Eattack <= 0:
            print("The enemy missed!")
        else:
            PlayerIG.health -= Eattack
            print("The enemy dealt %i damage!" % Eattack)
        option = input(' ')
        if PlayerIG.health <= 0:
            die()
        else:
            dunfight()






def ice():
    os.system('cls')
    print("Brrr.... It's cold in here!")
    option = input(' ')
    os.system('cls')
    print("%s says: Who even lives here?!" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    print("*BOOM*")
    time.sleep(3)
    print("%s Who goes there?" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    ifight()
def fire():
    os.system('cls')
    print("Whew! So Hot!")
    option = input(' ')
    os.system('cls')
    print("%s says: Why am I even here?!" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    print("*BOOM*")
    time.sleep(3)
    print("%s Who goes there?" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    ffight()

def earth():
    os.system('cls')
    print("It's so smelly in here!")
    option = input(' ')
    os.system('cls')
    print("%s says: The walls are all cracked!" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    print("*BOOM*")
    time.sleep(3)
    print("%s Who goes there?" % PlayerIG.name)
    option = input(' ')
    os.system('cls')
    efight()


def uplvl():
    lvlNext = 25
    if PlayerIG.xp >= lvlNext:
        PlayerIG.lvl += 1
        PlayerIG.maxhealth += 25
        PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.base_attack += 10
        PlayerIG.xp = PlayerIG.xp - lvlNext
        lvlNext = round(lvlNext * 1.5)
        print("You have leveled up to Level %i" % PlayerIG.lvl)
        option = input(' ')
        os.system('cls')
        


    else:
        pass
            

        

    
            
            
    
    
    
        
        
        
    
    
        

























main()
