# 3. Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    @property
    def income(self):
        return self.__income


class Position(Worker):

    def get_full_name(self):
        return f"{self.surname.capitalize()} {self.name.capitalize()}"

    def get_total_income(self):
        return sum(self.income.values())


pers1 = Position("Ivan", "ivanov", "worker", 30_000, -5_000)
pers2 = Position("petr", "petrov", "worker", 30_000, 1_500)
pers3 = Position("Vasiliy", "Vasiliev", "boss", 1_000_000, 500_000)

print(pers1.get_full_name())
print(pers1.get_total_income())
print()
print(pers2.get_full_name())
print(pers2.get_total_income())
print()
print(pers3.get_full_name())
print(pers3.get_total_income())
