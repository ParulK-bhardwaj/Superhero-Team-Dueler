# Inheritance Example
# class Animal:
#     def __init__(self, name, sleep_time):
#         self.name = name
#         self.sleep_time = sleep_time
    
#     def sleep(self):
#         print(f"{self.name} sleeps for hours {self.sleep_time}")

# class Dog(Animal):
#   def bark(self):
#     print("Woof! Woof!")

# my_dog = Dog("Sophie", 12)
# my_dog.sleep()
# my_dog.bark()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating!")
    
    def drink(self):
        print(f"{self.name} is drinking!")

class Frog(Animal):
    def jump(self):
        print(f"{self.name} is jumping!")

hoppy = Frog("Hoppy")

hoppy.eat()
hoppy.drink()
hoppy.jump()
        
