import random
from hero import Hero
from ability import Ability
# Team class that has the team of heroes

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        foundHero = False
        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
    
    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''
        for hero in self.heroes:
            print(f"Hero: {hero.name}")
    
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)
    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            hero_kill_death = round(hero.kills / hero.deaths, 2)
            print(f"{hero.name} Kill/Deaths:{hero_kill_death}")
    
    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        else:
            while len(living_heroes) > 0 and len(living_opponents)> 0:
                hero = random.choice(living_heroes)
                opponent = random.choice(living_opponents)
                hero.fight(opponent)
                if hero.is_alive() == False:
                    living_heroes.remove(hero)
                if opponent.is_alive() == False:
                    living_opponents.remove(opponent)
        