# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
import math
import time


class MyDivByZero(ZeroDivisionError):
    count = 0

    def __init__(self):
        MyDivByZero.count += 1
        print(f"Вы {MyDivByZero.count} {MyDivByZero.__util()} поделили на ноль!")

    @staticmethod
    def __util():
        i = MyDivByZero.count
        if 2 <= i % 10 <= 4 and (i % 100 < 12 or i % 100 > 14):
            return "раза"
        else:
            return "раз"


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def milt(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        try:
            if b == 0:
                raise MyDivByZero
            return a / b
        except MyDivByZero:
            return math.inf


for i in range(1500):
    print(Calculator.div(42, 0))
    time.sleep(0.5)
