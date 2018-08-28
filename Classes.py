from heroClass import *

myHero1 = HeroOf("Frodo", 20, "Elf")
myHero2 = HeroOf("Ron", 17, "wizard")
mySuperHero1 = SuperHeroOf("Ironman", 17, "humn", "Marvel")

myHero1.show_hero()
myHero1.move_hero()
myHero1.level_up()
myHero1.show_hero()

myHero2.show_hero()
myHero2.level_up()
myHero2.set_health(50)
myHero2.show_hero()

mySuperHero1.show_hero()
mySuperHero1.use_armo()
mySuperHero1.use_armo()
mySuperHero1.__armo = 11
mySuperHero1.use_armo()
mySuperHero1.show_hero()
