import random

from encapsulation import Warrior, Mage
class Knight(Warrior): #рыцарь
    def __init__(self, health=100, stamina=80, armor=20):
        super().__init__(health, stamina)
        self.armor = armor
    def introduces(self):
        super().introduces()
        print("---------------")
        print(f'Armor: {self.armor}')
        print("---------------")
    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        elif points <0:
            if self.armor > abs(points): #модуль abs
                self.armor += points
                print(f'Броня у {self.__class__.__name__} понижено до {self.armor}')
            elif self.armor < abs(points) and self.armor > 0:
                self.armor = 0
                print('Броня уничтожена')
                print(f'Здоровье у {target.__class__.__name__} понижено до {target.get_health()}')
            else:
                super().set_health(points)
    def __critical_hit(self, target): #критический урон
        target.set_health(-10)
        print('Сработал критиеский урон')
    def attacks(self, target):
        if random.randint(1,100) in range(1, 41):
            self.__critical_hit(target)
        else:
            super().attacks(target)
class Wizard(Mage):
    def __init__(self, health=100, mana=80, barrier=30):
        super().__init__(health, mana)
        self.barrier = barrier
    def set_health(self, points):
        if points > 0:
            super().set_health(points)
        elif points <0:
            if self.barrier > abs(points): #модуль abs
                self.barrier += points
                print(f'Барьер у {self.__class__.__name__} понижен до {self.barrier}')
            elif self.barrier < abs(points) and self.barrier > 0:
                self.barrier = 0
                print('Барьер уничтожен')

            else:
                super().set_health(points)
    def __fireball(self, target):
        target.set_health(-15)
        print('Сдработал огненный шар')
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.get_health()}')
    def attacks(self, target):
        if random.randint(1,100) in range(1, 21):
            self.__fireball(target)
        else:
            super().attacks(target)



unit1 = Knight(100, 80, 1)
unit2 = Warrior(100, 80)
unit3 = Knight(50, 0, 50)
unit4 = Wizard(100, 80, 1)

#unit2.attacks(unit1)
#unit1.attacks
