import random
from ability import Ability
from armor import Armor

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
    def fight(self, opponent):
        total_power = opponent.current_health + self.current_health
        my_winning_chance = self.current_health / total_power * 100
        if (random.randint(0, 100) < my_winning_chance):
            print(f"{self.name} defeats {opponent.name}!")
        else:
            print(f"{opponent.name} defeats {self.name}!")
    
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
        # return the total damage
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

# If we put the code inside the if __name__ == "__main__": block. This block will only run if this script is called directly. 
# The if/code block here prevents this block from being run when this script is imported by another script.
# Later we want to import the Hero class but we won't want to run this test code.
# if __name__ == "__main__":
#     ability = Ability("Great Debugging", 50)
#     another_ability = Ability("Smarty Pants", 90)
#     hero = Hero("Grace Hopper", 200)
#     hero.add_ability(ability)
#     hero.add_ability(another_ability)
#     armor = Armor("Great Suit", 80)
#     another_armor = Armor("Great blockers", 0)
#     hero.add_armor(armor)
#     hero.add_armor(another_armor)
#     print(hero.attack())
#     print(hero.defend())

if __name__ == "__main__":
    hero = Hero("Grace Hopper", 200)
    shield = Armor("Shield", 70)
    hero.add_armor(shield)
    hero.attack()
    hero.take_damage(500)
    print(hero.current_health)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())

