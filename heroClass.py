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