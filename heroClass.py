class HeroOf():
    """class for hero of the game"""
    def __init__(self, name, level, race):
        """init our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """Prints params of the hero"""
        descr = (self.name.title() + " of " + str(self.level) + " level with " + self.race + "race has " + str(self.health) + " health")
        print(descr)
    def level_up(self):
        """Rise level of the hero on one point"""
        self.level += 1
    def set_health(self, new_health):
        """Set new health to the hero"""
        self.health = new_health
    def move_hero(self):
        """Start moving hero"""
        print("Hero " + self.name + " started move")

class SuperHeroOf(HeroOf):
    """class for super hero"""
    def __init__(self, name, level, race, universe):
        """init our super hero"""
        super().__init__(name, level, race)
        self.universe = universe
        self.__armo = 100
    def use_armo(self):
        """using armo and decrease it by one point"""
        print(str(self.name) + " is using armo")
        self.__armo-= 1
        print(str(self.__armo) + " lefted")
    def show_hero(self):
        """Prints params of the hero"""
        descr = (self.name.title() + " of " + str(self.level) + " level with " + self.race + 
                "race has " + str(self.health) + " health and belongs to " + self.universe.title() + " universe")
        print(descr)