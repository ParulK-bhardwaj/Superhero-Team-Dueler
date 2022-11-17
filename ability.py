import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = int(max_damage)
    
    def attack(self):
    # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())