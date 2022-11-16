from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        team_one: None
        team_two: None
    
    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("What is the ability name?  ")
        max_damage = input("What is the max damage of the ability?  ")
        return Ability(name, max_damage)
    
    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        name = input("What is the weapon name?  ")
        max_damage = input("What is the max damage of the weapon?  ")
        return Weapon(name, max_damage)

    def create_armor(self):
        '''Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("What is the armor name?  ")
        max_block = input("What is the max blocking power of the armor?  ")
        return Armor(name, max_block)

    def create_hero(self):
        '''Prompt user for Hero information
        return Hero with values from user input.
        '''
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                ability1 = self.create_ability()
                hero.add_ability(ability1)
            elif add_item == "2":
                weapon1 = self.create_weapon()
                hero.add_weapon(weapon1)
            elif add_item == "3":
                armor1 = self.create_armor()
                hero.add_armor(armor1)
        return hero
    
    # build_team_one is provided to you
    def build_team_one(self):
        '''Prompt the user to build team_one '''
    # This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.
    # Add the created hero to team one.
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two'''
        numberOfTeamMembers2 = int(input("How many members would you like on Team Two?\n"))
        for i in range(numberOfTeamMembers2):
            hero2 = self.create_hero()
            self.team_two.add_hero(hero2)
    
    def team_battle(self):
        '''Battle team_one and team_two together.'''
        self.team_one.attack(self.team_two)
    
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        # TODO: This method should print out battle statistics
        # including each team's average kill/death ratio.
        # Required Stats:
        #     Show surviving heroes.
        #     Declare winning team
        #     Show both teams average kill/death ratio.
        # Some help on how to achieve these tasks:
        # TODO: for each team, loop through all of their heroes,
        # and use the is_alive() method to check for alive heroes,
        # printing their names and increasing the count if they're alive.
        for hero in self.team_one:
            if hero.is_alive():
                print(hero.name)
        for hero in self.team.two:
            if hero.is_alive():
                print(hero.name)
        # TODO: based off of your count of alive heroes,
        # you can see which team has more alive heroes, and therefore,
        # declare which team is the winning team
        #
        # TODO for each team, calculate the total kills and deaths for each hero,
        # find the average kills and deaths by dividing the totals by the number of heroes.
        # finally, divide the average number of kills by the average number of deaths for each team

        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # Calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

        # Display the average K/D for Team Two
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))
        # list the heroes from Team One that survived
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)


if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()