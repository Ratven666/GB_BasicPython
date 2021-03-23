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

    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, size):
        self.__size = size
        super().__init__(name)
        Clothes.total_consumption += self.__size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        self.__height = height
        super().__init__(name)
        Clothes.total_consumption += 2*self.__height + 0.3


coat1 = Coat("firma1", 42)
print(Clothes.total_consumption)
coat2 = Coat("firma2", 28)
print(Clothes.total_consumption)
suit1 = Suit("firma3", 1.20)
print(Clothes.total_consumption)
suit2 = Suit("firma4", 1.80)
print(Clothes.total_consumption)





