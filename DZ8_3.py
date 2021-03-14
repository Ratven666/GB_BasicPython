# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    """
    Обертка логирующая тип переданных аргументов
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        print(f"{func.__name__}(")
        for arg in args:
            print(f"{arg}: {type(arg)}", end=", ")
        print("\b\b")
        for k, v in kwargs.items():
            print(f"[{k}] {v}: {type(v)}")
        print(")")
        print("____end_wrapper____")
        return func(*args, **kwargs)
    return wrapper


@type_logger
def calc_cube(x, y):
    """
    Возводит число в куб
    :param x: число
    :param y: просто для того чтобы что-то передать
    :return: куб числа
    """
    return x ** 3


@type_logger
def print_pet_names(*owners, **pets):
    """
    Выводит в косоль имена хозяев и их животных их типу
    :param owners: хозяева (неименованые типом аргументы)
    :param pets: (именованые аргументы - тип=имя)
    :return:
    """
    print(f"Owners Name: {owners}")
    for pet, name in pets.items():
        print(f"{pet}: {name}")


print_pet_names("Mike", "Ksu", dog="Gauss", cat="Bessel")
print()
print(calc_cube(5, "qwe"))
