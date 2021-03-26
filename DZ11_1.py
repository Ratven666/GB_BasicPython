# 1. Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
#
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц,
# год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data: str):
        temp = Data.pars_data_string(data)
        if Data.check_data(temp):
            self.day, self.month, self.year = temp
        else:
            raise ValueError("Неправильная дата в строке")


    @classmethod
    def pars_data_string(cls, data: str):
        return [int(i) for i in data.split("-")]

    @staticmethod
    def check_data(data: list):
        if data[0] <= 0 or data[0] > 31:
            return False
        if data[1] <=0 or data[1] > 12:
            return False
        return True

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


data = Data("06-12-1988")
print(data)
data2 = Data("06-13-1988")
print(data2)