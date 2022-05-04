class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health #здоровье
        self.stamina = stamina #жизненные силы
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if self.health > 100:
            self.__health = 100
        elif self.health < 0:
            self.__health = 0
        else:
            self.__health = new_health


    def introduces(self):
        print("---------------")
        print(f'class: {self.__class__.__name__}') #дает имя класса
        print(f'health: {self.health}')
        print(f'stamina: {self.stamina}')
        print("---------------")

    def heals(self,target):
        print("---------------")
        print(f'{self.__class__.__name__} накладывает повязку из целебных трав'
              f' {target.__class__.__name__}')
        target.health += 10
        self.stamina -= 20
        print(f'Здоровье у {target.__class__.__name__} повышено {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.stamina} запаса сил')
        print("---------------")

    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} наносит урон мечом'
              f' {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print("---------------")


class Mage:
    def __init__(self, health=60, mana=100): #дефолтное значение
        self.health = health #уровень здоровья
        self.mana = mana #атрибут (уровень магии)
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health):
        if self.health > 100:
            self.__health = 100
        elif self.health < 0:
            self.__health = 0
        else:
            self.__health = new_health

    def introduces(self):
        print("---------------")
        print(f'class: {self.__class__.__name__}') #дает имя класса
        print(f'health: {self.health}')
        print(f'mana: {self.mana}')
        print("---------------")

    def heals(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} применяет заклинание лечения'
              f' к {target.__class__.__name__}')
        target.health += 10
        self.mana -= 20
        print(f'Здоровье у {target.__class__.__name__} увеличилось до {target.health}')
        print(f'У {self.__class__.__name__} осталось {self.mana} единиц магии')
        print("---------------")

    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} наносит урон магией'
              f' {target.__class__.__name__}')
        target.health -= 3
        print(f'Здоровье у {target.__class__.__name__} понижено до {target.health}')
        print("---------------")


unit1 = Warrior(100, 50) #объект класса воинов
# print(unit1.__dict__)
# unit1.introduces()


unit2 = Warrior() #второй класс воинов
# print(unit2.__dict__)
# unit2.introduces()

unit3 = Mage(70,70) #второй класса мага
# print(unit3.__dict__)
# unit3.introduces()
# unit3.heals(unit1)
# unit3.attacks(unit1)

unit4 = Mage() #второй класса мага
# print(unit4.__dict__)
# unit4.introduces()
# unit1.heals(unit4)
# unit1.attacks(unit3)




