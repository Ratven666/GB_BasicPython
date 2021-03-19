# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.__speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print(f"Машина {self.name} поехала!")

    def stop(self):
        print(f"Машина {self.name} остановилась!")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}!")

    def show_speed(self):
        print(self.__speed)

    @property
    def speed(self):
        return self.__speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышении скорости!")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышении скорости!")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args)
        self.is_police = True

    def show_speed(self):
        print("Полиция может ехать как хочет)")


town_car1 = TownCar(45, "red", "Steve")
town_car2 = TownCar(65, "green", "Mack")

work_car1 = WorkCar(35, "black", "Jack")
work_car2 = WorkCar(50, "blue", "Jho")

sport_car = SportCar(120, "pink", "Jill")
police_car = PoliceCar(666, "white", "Cop")

town_car1.go()
town_car1.show_speed()
print()
town_car2.go()
town_car2.show_speed()
print()
work_car1.go()
work_car1.show_speed()
print()
work_car2.go()
work_car2.show_speed()
print()
sport_car.go()
sport_car.show_speed()
print()
police_car.go()
police_car.show_speed()
