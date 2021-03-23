# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    total_consumption = 0
    __cash_obj = []

    def __init__(self, name):
        self.__name = name

    @classmethod
    def add_consumption(cls, *clothes):
        for item in clothes:
            if item not in cls.__cash_obj:
                cls.total_consumption += item.calc_material_consumption()
                cls.__cash_obj.append(item)

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def calc_material_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)

    def calc_material_consumption(self):
        return self.__size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.__height = height
        super().__init__(name)

    def calc_material_consumption(self):
        return 2*self.__height + 0.3


coat1 = Coat("firma1", 42)
coat2 = Coat("firma2", 28)
suit1 = Suit("firma3", 1.20)
suit2 = Suit("firma4", 1.80)

print(coat1.calc_material_consumption(), coat1.name)
print(coat2.calc_material_consumption(), coat2.name)
print(suit1.calc_material_consumption(), suit1.name)
print(suit2.calc_material_consumption(), suit2.name)

print("========================")

Clothes.add_consumption(coat1)
print(Clothes.total_consumption)
Clothes.add_consumption(coat2)
print(Clothes.total_consumption)
Clothes.add_consumption(suit2)
print(Clothes.total_consumption)
Clothes.add_consumption(suit1)
print(Clothes.total_consumption)

print("========================")

Clothes.add_consumption(coat1)
print(Clothes.total_consumption)
Clothes.add_consumption(coat1)
print(Clothes.total_consumption)
Clothes.add_consumption(coat2)
print(Clothes.total_consumption)
Clothes.add_consumption(suit2)
print(Clothes.total_consumption)



