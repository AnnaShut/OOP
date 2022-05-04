class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health #здоровье
        self.__stamina = stamina #жизненные силы

    def get_health(self):
        return self.__health

    def set_health(self, points):
        self.__health += points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0


    def introduces(self):
        print("---------------")
        print(f'class: {self.__class__.__name__}') #дает имя класса
        print(f'health: {self.get_health()}')
        print(f'stamina: {self.__stamina}')
        print("---------------")

    def heals(self,target):
        print("---------------")
        print(f'{self.__class__.__name__} накладывает повязку из целебных трав'
              f' {target.__class__.__name__}')
        if self.__stamina >= 20:
            target.set_health(10)
            self.__stamina -= 20
            print(f'Здоровье у {target.__class__.__name__} повышено до {target.get_health()}')
            print(f'У {self.__class__.__name__} осталось {self.__stamina} запаса сил')
        else:
            print('Недостаточно сил')
        print("---------------")

    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} наносит урон мечом'
              f' {target.__class__.__name__}')
        if target.get_health() > 3:
            target.set_health(-3)
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.get_health()}')
        else:
            target.set_health(-3)
            print(f'{self.__class__.__name__} наносит последний удар и побеждает'
                  f' {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
        print("---------------")


class Mage:
    def __init__(self, health=60, mana=100): #дефолтное значение
        self.__health = health #уровень здоровья
        self.__mana = mana #атрибут (уровень магии)

    def get_health(self):
        return self.__health

    def set_health(self, points):
        self.__health -= points
        if self.__health > 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0


    def introduces(self):
        print("---------------")
        print(f'class: {self.__class__.__name__}') #дает имя класса
        print(f'health: {self.__health}')
        print(f'mana: {self.__mana}')
        print("---------------")

    def heals(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} применяет заклинание лечения'
              f' к {target.__class__.__name__}')
        if self.__mana >= 20:
            target.set_health(10)
            self.__mana -= 20
            print(f'Здоровье у {target.__class__.__name__} увеличилось до {target.get_health()}')
            print(f'У {self.__class__.__name__} осталось {self.__mana} единиц магии')
        else:
            print('Недостаточно магии')
        print("---------------")

    def attacks(self, target):
        print("---------------")
        print(f'{self.__class__.__name__} наносит урон магией'
              f' {target.__class__.__name__}')
        if target.get_health() > 3:
            target.set_health(-3)
            print(f'Здоровье у {target.__class__.__name__} понижено до {target.get_health()}')
        else:
            target.set_health(-3)
            print(f'{self.__class__.__name__} наносит последний удар и побеждает'
                  f' {target.__class__.__name__}')
            print(f'{target.__class__.__name__} покидает отряд')
        print("---------------")


unit1 = Warrior(2, 10) #объект класса воинов
# print(unit1.__dict__)
# unit1.introduces()


unit2 = Warrior() #второй класс воинов
# print(unit2.__dict__)
# unit2.introduces()

unit3 = Mage(50,10) #второй класса мага
# print(unit3.__dict__)
# unit3.introduces()
# unit3.heals(unit1)
# unit3.attacks(unit1)

unit4 = Mage() #второй класса мага
# print(unit4.__dict__)
# unit4.introduces()
# unit1.heals(unit4)
# unit1.attacks(unit3)
# print(unit4.get_health())
# unit2.heals(unit1)
# # unit1.attacks(unit3)
# unit1.heals(unit3)
# unit3.heals(unit1)
# unit1.attacks(unit3)
# unit3.attacks(unit1)
# unit1.heals(unit3)
# unit3.heals(unit1)

