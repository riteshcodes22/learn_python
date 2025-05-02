import os
import random
import time
import sys
from colorama import Fore, Style

class Hero:
    def __init__(self,name, power,health, max_health, about):
        self.name = name
        self.power = power
        self.health = health
        self.max_health = max_health
        self.about = about

    def __str__(self):
        return f"{self.name} is {self.about.lower()} with Power: {self.power}, Health: {self.health}/{self.max_health}"
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,enemy):
        enemy.health -= self.power
        if enemy.health < 0:
            enemy.health = 0
        print(f"{self.name} is attacking {enemy.name}")
        if not enemy.is_alive():
            print(f"{enemy.name} defeated by {self.name}")
        print(f"{enemy.name}'s health is now {enemy.health}")
    
    def heal(self):
        heal_points = 15
        if not self.is_alive():
            print(f"{self.name} is not alive and hence can't be healed")
        elif self.health == self.max_health:
               print(f"{self.name} is already at full health.")
        else:
            temp = self.health
            self.health += heal_points
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"{self.name} is healed by {temp - self.health} points. Health is now {self.health}")
       
hero1 = Hero("Ironblade", power=20, health=100, max_health=100,
             about="A balanced warrior with solid offense and defense.")
hero2 = Hero("Nightshade", power=15, health=110, max_health=110,
             about="A stealthy assassin with resilience and precision.")
hero3 = Hero("Stormcaller", power=25, health=90, max_health=90,
             about="A powerful mage who trades defense for high damage.")
hero4 = Hero("Thunderhoof", power=18, health=120, max_health=120,
             about="A beast with raw endurance and stable damage.")
hero5 = Hero("Asharrow", power=22, health=95, max_health=95,
             about="A swift ranger striking from the shadows.")
hero6 = Hero("Grimwarden", power=16, health=130, max_health=130,
             about="A sturdy tank who wears enemies down.")
hero7 = Hero("Emberfist", power=28, health=80, max_health=80,
             about="An explosive brawler with incredible burst power.")
hero8 = Hero("Frostveil", power=17, health=115, max_health=115,
             about="A steady combatant with balanced tactics.")
hero9 = Hero("Voidstriker", power=24, health=85, max_health=85,
             about="A shadowy figure who strikes quickly and vanishes.")
hero10 = Hero("Sunblade", power=20, health=100, max_health=100,
              about="A noble knight shining with balance and courage.")

heroes = [hero1, hero2, hero3, hero4, hero5, hero6, hero7, hero8, hero9,hero10]

# Function to create the typewriter effect in python output terminal
def typewriter_effect(sentence, type_delay = 0.05, delete_delay = 0.01):
    # Loop through each character in the sentence
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

    # Pause after printing the entire sentence
    time.sleep(1)

    # Loop to delete the sentence
    for _ in sentence:
        # Write backspace, space, delete and delay
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(delete_delay)

def coin_toss():
    your_choice = input("Press 'h' for heads or 't' for tails")
    if your_choice.lower() == 'h' or your_choice.lower() =='t':
        if your_choice == random.choice(['h','t']):
            return True
        else:
            return False
    else:
        print('wrong input')
        coin_toss()

def heroes_table(heroes):
    print(Fore.LIGHTMAGENTA_EX + "-" * 140)
    print(f"{Fore.BLUE + 'HERO_ID':<15} {'NAME':<15} {'POWER':<12} {'HEALTH':<12} {'MAX HEALTH':<15} {'ABOUT':<15}")
    print(Fore.LIGHTMAGENTA_EX + "-" * 140)
    for idx, hero in enumerate(heroes,start=1):
        print(f"{idx: <8} {hero.name:<18} {hero.power:<12} {hero.health:<15} {hero.max_health:<11} {hero.about}")
    print(Style.RESET_ALL)

def choose_hero(heroes):
    
    while True:
        heroes_table(heroes)
        your_choice = input("Choose a number between 1 and 10 to select your corresponding warrior: ")
        try:
            your_choice = int(your_choice)
            break
        except ValueError: 
            print("Invalid input. please try again.")

    if your_choice >= 1 and your_choice <=10:
        temp_list = list(range(1,11))
        temp_list.remove(your_choice)
        computer_choice = random.choice(temp_list)
        choices = {'user_hero': f"hero{str(your_choice)}", 'computer_hero': f"hero{str(computer_choice)}"}
        return choices
    else:
        print("Wrong input")
        return choose_hero(heroes)

def battle(heroes):
    typewriter_effect(Fore.YELLOW + "Long ago, in the shadowed valleys of feudal Japan. . .")
    typewriter_effect(Fore.YELLOW + "There existed a sacred tradition known only to the most elite warriors")
    typewriter_effect(Fore.BLUE + "THE TENFOLD DUEL",0.1)
    typewriter_effect(Fore.YELLOW + "Every generation, the ten greatest fighters across the provinces were summoned by a secretive brotherhood of sages")
    typewriter_effect(Fore.YELLOW + "Each warrior was unmatched in skill, honor and will")
    typewriter_effect(Fore.YELLOW + "But to be remembered as the greatest, one had to prove it in the",0.05,0.0001)
    typewriter_effect(Fore.BLUE + "DOJO OF SHADOWS",0.1)
    typewriter_effect(Fore.YELLOW + "a hidden arena carved into the heart of MOUNT KAMINARI")
    typewriter_effect(Fore.BLUE + "not for land, not for lords, but for legacy",0.1)

    typewriter_effect(Fore.GREEN + "Loading Game . . .")
    typewriter_effect(Fore.GREEN + "5 4 3 2 1", 0.25)

    choices = choose_hero(heroes)
    os.system('cls')
    typewriter_effect(Fore.RED + f"You as {choices['user_hero']} VS {choices['computer_hero']}")
    typewriter_effect(Fore.YELLOW + "Coin toss to determine who goes first")

    toss_result = coin_toss()

    
battle(heroes)
print(Style.RESET_ALL)