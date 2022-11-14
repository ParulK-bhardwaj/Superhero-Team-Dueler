import random
from ability import Ability
from armor import Armor
from weapon import Weapon
from team import Team

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name #String
        self.starting_health = starting_health #Integer
        self.current_health = starting_health #Integer
    ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
#   Stretch challenge 1
    # def fight(self, opponent):
    #     list = [opponent.name, self.name]
    #     winner = random.choice(list)
    #     if winner == opponent.name:
    #         print(f"{winner} defeats {self.name}!")
    #     else:
    #         print(f"{winner} defeats {opponent.name}!")
#   Stretch challenge 2
    # def fight(self, opponent):
    #     total_power = opponent.current_health + self.current_health
    #     my_winning_chance = self.current_health / total_power * 100
    #     if (random.randint(0, 100) < my_winning_chance):
    #         print(f"{self.name} defeats {opponent.name}!")
    #     else:
    #         print(f"{opponent.name} defeats {self.name}!")
    
    def add_ability(self, ability):
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)
    
    '''Calculate the total damage from all ability attacks.
      return: total_damage:Int
  '''
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
        # add the damage of each attack to our running total
            total_damage += ability.attack()
        return total_damage
    '''Add armor to self.armors
        Armor: Armor Object
    ''' 
    def add_armor(self, armor):
        self.armors.append(armor)

    '''Calculate the total block amount from all armor blocks.
     return: total_block:Int
    '''
    def defend(self):
        total_defence = 0
        for armor in self.armors:
            total_defence += armor.block()
        return total_defence
    
    def take_damage(self, damage):
        damage_on_attack = damage - self.defend()
        if damage_on_attack <= 0:
            self.current_health = self.current_health
        else:
            self.current_health -= damage_on_attack
        return self.current_health

    def is_alive(self):  
        if self.current_health < 0:
            return False
        else:
            return True
    
    # 0) Check if at least one hero has abilities. If no hero has abilities, print "Draw"
    # 1) else, start the fighting loop until a hero has won
    # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
    # 3) After each attack, check if either the hero (self) or the opponent is alive
    # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
    
    def fight(self, opponent):
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw")
        else:
            # loop runs till both the hero and opponent is alive
            while self.is_alive() and opponent.is_alive():
                if len(self.abilities) >= 1:
                    total_damage = self.attack()
                    opponent.take_damage(total_damage)
                if len(opponent.abilities) >= 1:
                    total_damage = opponent.attack()
                    self.take_damage(total_damage)
                    if self.is_alive() and opponent.is_alive() == False:
                        print(f"{self.name} won!")
                    elif self.is_alive() == False and opponent.is_alive():
                        print(f"{opponent.name} won!")
                    elif self.is_alive() == False and opponent.is_alive() == False:
                        print("Noone has won! Both the heroes have lost!")

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''
        self.abilities.append(weapon)

# If we put the code inside the if __name__ == "__main__": block. This block will only run if this script is called directly. 
# The if/code block here prevents this block from being run when this script is imported by another script.
# Later we want to import the Hero class but we won't want to run this test code.

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())

    # define an ability and a weapon
    # both have the same max damage
    eye_rays = Ability('Eye Rays', 50)
    laser_blast = Weapon('Laser Blast', 50)

    # Let's put these in an array together
    # This list contains different types: Ability and Weapon
    powers = [eye_rays, laser_blast]

    # We know that all Abilities and Weapons share the same attribute
    for power in powers:
        print(power.max_damage)

    # We know that all Abilities and Weapns implement the attack method
    for power in powers:
        print(power.attack())

# Note! While both implement attack() a Weapon will always return 
# a higher average damage!

# if __name__ == "__main__":
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 30)
    # ability2 = Ability("Super Eyes", 30)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)


# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.

#     hero = Hero("Grace Hopper", 200)
#     hero.take_damage(150)
#     print(hero.is_alive())
#     hero.take_damage(15000)
#     print(hero.is_alive())

