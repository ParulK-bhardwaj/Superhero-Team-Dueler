from ability import Ability
import random

class Weapon(Ability):
  def attack(self):
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    min_damage = self.max_damage // 2
    weapon_attack_power = random.randint(min_damage, self.max_damage)
    return weapon_attack_power

if __name__ == "__main__":
    weapon = Weapon("Debugging Ability", 20)
    print(weapon.name)
    print(weapon.attack())