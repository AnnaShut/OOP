from game_classes import Warrior, Mage

class Archer(Warrior):
    def __init__(self, health=100, stamina=100, arrows=20):
        super().__init__(health, stamina)
        self.arrows = arrows

    def introduces(self):
        super().introduces()
        print("---------------")
        print(f'Arrows: {self.arrows}')
        print("---------------")

    def attacks (self, target):
        print("---------------")
        print(f'{self.__class__.__name__} использует лук против'
              f' {target.__class__.__name__}')
        target.health -= 4
        self.arrows -= 1
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.arrows} стрел')
        print("---------------")

class Alchemist(Mage):
    def __init__(self, health=100, mana=100, flasks=10):
        super(). __init__(health, mana)
        self.flasks = flasks
    def attacks (self, target):
        print("---------------")
        print(f'{self.__class__.__name__} использует бутыль с огнем против'
              f' {target.__class__.__name__}, но при этом задевает себя')
        target.health -= 10
        self.health -= 3
        self.flasks -= 1
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print(f'Здоровье у {self.__class__.__name__} понижено до {self.health}')
        print(f'У {self.__class__.__name__} осталось {self.flasks} алхимических бутылей')
        print("---------------")


unit1 = Archer()
unit2 = Archer()
unit3 = Warrior()
unit4 = Alchemist()
# print(unit1.__dict__)
# unit2.heals(unit1)
# unit2.attacks(unit3)
# unit1.introduces()
unit4.attacks(unit3)