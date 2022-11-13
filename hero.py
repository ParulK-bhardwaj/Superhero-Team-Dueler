import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name #String
        self.starting_health = starting_health #Integer
        self.current_health = starting_health #Integer
    ''' Current Hero will take turns fighting the opponent hero passed in.
  '''
    def fight(self, opponent):
        self.opponent = opponent
        list = [self.opponent, self.name]
        winner = random.choice(list)
        if winner == self.opponent:
            print(f"{winner} defeats {self.name}!")
        else:
            print(f"{winner} defeats {self.opponent}!")

# If we put the code inside the if __name__ == "__main__": block. This block will only run if this script is called directly. 
# The if/code block here prevents this block from being run when this script is imported by another script.
# Later we want to import the Hero class but we won't want to run this test code.
if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2.name)