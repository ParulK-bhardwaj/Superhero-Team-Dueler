import random

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = int(max_block)

    def block(self):
        block_random_value = random.randint(0, self.max_block)
        return block_random_value

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())
