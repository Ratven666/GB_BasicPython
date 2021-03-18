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
    def __init__(self, name: str, surname: str, position, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.__bonus = bonus

    def get_full_name(self):
        return f"{self.surname.capitalize()} {self.name.capitalize()}"

    def get_total_income(self):
        return sum(self.position.income.values()) + self.__bonus


class Position:
    def __init__(self, position, wage):
        self.__position = position
        self.__income = {"wage": wage}

    @property
    def income(self):
        return self.__income

    @property
    def position(self):
        return self.__position


worker = Position("worker", 30_000)
boss = Position("boss", 1_000_000)

pers1 = Worker("Ivan", "ivanov", worker, -5_000)
pers2 = Worker("petr", "petrov", worker, 1_500)
pers3 = Worker("Vasiliy", "Vasiliev", boss, 500_000)


print(pers1.get_full_name())
print(pers1.get_total_income())
print()
print(pers2.get_full_name())
print(pers2.get_total_income())
print()
print(pers3.get_full_name())
print(pers3.get_total_income())

pers1.position = boss
pers3.position = worker

print("=========================")
print(pers1.get_full_name())
print(pers1.get_total_income())
print()
print(pers3.get_full_name())
print(pers3.get_total_income())
