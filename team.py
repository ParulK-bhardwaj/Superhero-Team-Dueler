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
            print(hero.name)
        # TODO: Loop over the list of heroes and print their names to the terminal one by one.
    
    def add_hero(self, hero):
        '''Add Hero object to self.heroes.'''
        self.heroes.append(hero)