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

    def attack(self,enemy,is_user):
        enemy.health -= self.power
        if enemy.health < 0:
            enemy.health = 0
        color = Fore.GREEN if is_user else Fore.RED
        typewriter_effect_new(color + f"{self.name} is attacking {enemy.name}.")
        typewriter_effect_new(color + f"{enemy.name}'s health is now {enemy.health}.")

        if not enemy.is_alive():
            print("\n")
            typewriter_effect_new(color + f"{enemy.name} defeated by {self.name}.")

    
    def heal(self, is_user):
        heal_points = 15
        color = Fore.GREEN if is_user else Fore.RED
        if not self.is_alive():
            typewriter_effect(color + f"{self.name} is not alive and hence can't be healed.")
        elif self.health == self.max_health:
               typewriter_effect_new(color + f"{self.name} is already at full health.")
        else:
            temp = self.health
            self.health += heal_points
            if self.health > self.max_health:
                self.health = self.max_health
            typewriter_effect_new(color + f"{self.name} is healed by {self.health - temp} points. Health is now {self.health}.")
       
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
def typewriter_effect_new(sentence, type_delay = 0.05, delete_delay = 0.01):
    # Loop through each character in the sentence
    for char in sentence:

        # Write, display and delay
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(type_delay)

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

def is_coin_toss():
    while True:
        choice = input("Press 'h' for heads or 't' for tails: ")
        choice = choice.strip().lower()
        if choice in ('h','t'):
            if choice == random.choice(['h','t']):
                typewriter_effect(Fore.GREEN + "You won the toss")
                return True
            else:
                typewriter_effect(Fore.RED + "You lost the toss")
                return False
        else:
            typewriter_effect(Fore.YELLOW + "Wrong input")

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
            if your_choice >= 1 and your_choice <=10:
                temp_list = list(range(1,11))
                temp_list.remove(your_choice)
                computer_choice = random.choice(temp_list)

                user_hero = heroes[your_choice-1]
                computer_hero = heroes[computer_choice-1]
                return user_hero, computer_hero
            else:
                typewriter_effect(Fore.YELLOW + "Wrong input")
                break
        except ValueError: 
            typewriter_effect(Fore.YELLOW + "Invalid input. please try again.")

def attack_or_heal(user_hero,computer_hero,is_user_turn,is_first_turn):
    if is_user_turn:
        if is_first_turn:
            user_hero.attack(computer_hero,is_user_turn)
        else:
            while True:
                print(Fore.BLUE)
                choice = input("enter 'a' to attack or 'h' to heal: ")
                choice = choice.strip().lower()
                if choice == 'h':
                    user_hero.heal(is_user_turn)
                    break
                elif choice == 'a':
                    user_hero.attack(computer_hero,is_user_turn)
                    break
                else:
                    typewriter_effect(Fore.LIGHTMAGENTA_EX + "Wrong input")
    else:
        if is_first_turn:
            computer_hero.attack(user_hero,is_user_turn)
        else:
            typewriter_effect_new(Fore.RED + f"{computer_hero.name} is choosing to attack or heal.")
            choice = random.choice(['a','h'])
            if choice == 'h':
                computer_hero.heal(is_user_turn)
            else:
                computer_hero.attack(user_hero,is_user_turn)

def health_bar(hero):
    char = '🟩'  # Green for user, red for computer
    char_fill = '⬜'
    bar_length = 20
    fill_ratio = hero.health / hero.max_health
    fill_count = int(fill_ratio * bar_length)
    return char * fill_count + char_fill * (bar_length - fill_count)

def health_bar_line(user_hero, computer_hero):
    user_bar = health_bar(user_hero)
    comp_bar = Fore.RED + health_bar(computer_hero)

    print()
    print(Fore.GREEN + f"{user_hero.name}{user_bar} {user_hero.health}/{user_hero.max_health}",end='\t\t')
    print(Fore.RED + f"{computer_hero.name}{comp_bar} {computer_hero.health}/{computer_hero.max_health}")
    print()

            
def battle_loop(user_hero, computer_hero, is_user_turn):
    is_first_turn = True
    turn_count = 0
    round_num = 1

    while user_hero.health > 0 and computer_hero.health > 0:
        
        # After every 2 turns (one round), show a round separator
        if turn_count % 2 == 0:
            print(Fore.LIGHTMAGENTA_EX + "-" * 150)
            print(Fore.LIGHTMAGENTA_EX + f"{'ROUND ' + str(round_num):^140}")
            print(Fore.LIGHTMAGENTA_EX + "-" * 150)
            round_num += 1

        attack_or_heal(user_hero, computer_hero, is_user_turn, is_first_turn)
        health_bar_line(user_hero, computer_hero)

        turn_count += 1
        is_user_turn = not is_user_turn
        is_first_turn = False

        

    # Result announcement
    if user_hero.health == 0 and computer_hero.health == 0:
        typewriter_effect_new(Fore.YELLOW + "It's a draw")
    elif computer_hero.health == 0:
        typewriter_effect_new(Fore.GREEN + "YOU WIN!!!")
    else:
        typewriter_effect_new(Fore.RED + "You Loose")

def is_story_mode(choice):
    if choice:
        typewriter_effect(Fore.YELLOW + "Long ago, in the shadowed valleys of feudal Japan. . .")
        typewriter_effect(Fore.YELLOW + "There existed a sacred tradition known only to the most elite warriors")
        typewriter_effect(Fore.BLUE + "THE TENFOLD DUEL",0.1)
        typewriter_effect(Fore.YELLOW + "Every generation, the ten greatest fighters across the provinces were summoned by a secretive brotherhood of sages")
        typewriter_effect(Fore.YELLOW + "Each warrior was unmatched in skill, honor and will")
        typewriter_effect(Fore.YELLOW + "But to be remembered as the greatest, one had to prove it in the",0.05,0.0001)
        typewriter_effect(Fore.BLUE + "DOJO OF SHADOWS",0.1)
        typewriter_effect(Fore.YELLOW + "a hidden arena carved into the heart of MOUNT KAMINARI")
        typewriter_effect(Fore.RED + "not for land, not for lords, but for legacy",0.1)

def battle(heroes):
    typewriter_effect_new(Fore.LIGHTMAGENTA_EX + 'Welcome to "THE TENFOLD HONOR 十倍の栄誉"')
    print()
    typewriter_effect_new(Fore.BLUE + "Choose 's' for story mode or 'q' for quick match: ")
    choice = input()
    choice = choice.strip().lower()
    while True:
        if choice in (['s', 'q']):
            if choice == 's':
                is_story_mode(choice)
                break
            else:
                break
        else:
            typewriter_effect("Wrong input")

    typewriter_effect(Fore.GREEN + "Loading Game . . .")
    typewriter_effect(Fore.GREEN + "5...4...3...2...1...")

    user_hero, computer_hero = choose_hero(heroes)

    print("You as",end=" ")
    print(Fore.GREEN + f"{user_hero.name}",end=" ") 
    print(Fore.BLACK + "VS",end= " ")
    print(Fore.RED + f"{computer_hero.name}")

    typewriter_effect(Fore.YELLOW + "Coin toss to determine who goes first")

    is_user_turn = is_coin_toss()
    battle_loop(user_hero,computer_hero,is_user_turn)


    
battle(heroes)
print(Style.RESET_ALL)