import random

class Hero:
    def __init__(self, name, starting_health=100):
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

# If we put the code inside the if __name__ == "__main__": block. This block will only run if this script is called directly. 
# The if/code block here prevents this block from being run when this script is imported by another script.
# Later we want to import the Hero class but we won't want to run this test code.
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman", 300)
    hero2 = Hero("Dumbledore", 250)
    hero1.fight(hero2)