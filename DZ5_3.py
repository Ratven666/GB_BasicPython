tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

klasses = [
    '9А', '7В', '9Б', '9В'
]


def school_generator(tutors: list, klasses: list) -> tuple:
    """
    Генератор, возвращающий кортежи вида (<tutor>, <klass>)
    :param tutors: Список учителей
    :param klasses: Список классов
    :return: (tuple) (Учитель, класс) или (Учитель, None), если классы закончились
    """
    for index, tutor in enumerate(tutors):
        if index < len(klasses):
            yield tutor, klasses[index]
        else:
            yield tutor, None


gen = school_generator(tutors, klasses)

print(type(gen))

for el in gen:
    print(el)

"""
Для школы не знаю, но по такому принципу можно организовывать запись когда желающих больше чем мест,
например к врачу или что-то такое...
Вызывает ассоциации с очередью или чем-то таким
"""


