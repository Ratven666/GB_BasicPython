# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Пишем текст")


class Pencil(Stationery):
    def draw(self):
        print("Рисум рисунок")


class Handle(Stationery):
    def draw(self):
        print("Выделяем текст")


s1 = Stationery("stationery")
s2 = Pen("pen")
s3 = Pencil("pencil")
s4 = Handle("handle")

s1.draw()
s2.draw()
s3.draw()
s4.draw()
