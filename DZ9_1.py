# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить
# соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    __color = ["красный", "жёлтый", "зелёный"]

    def __init__(self, red_delay=7, yellow_delay=2, green_delay=4):
        self.delays = [red_delay, yellow_delay, green_delay]

    def running(self):
        for i, color in enumerate(TrafficLight.__color):
            print(color)
            TrafficLight.__print_time(self.delays[i])

    @staticmethod
    def __print_time(sec):
        for i in range(sec):
            time.sleep(1)
            print(i+1)


tl1 = TrafficLight()
tl2 = TrafficLight(4,3,5)
tl1.running()
print("===============")
tl2.running()
