# 4. * Написать декоратор с аргументом-функцией (callback),
# позволяющий валидировать входные значения функции и выбрасывать исключение
# ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?

def val_checker(l_func):
    def _val_checker(funk):
        def wrapper(*args):
            for arg in args:
                if not l_func(arg):
                    raise ValueError
            return funk(*args)
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


@val_checker(lambda x: type(x) is str)
def string_capitalizer(string: str):
    return string.capitalize()


print(string_capitalizer("qwerty"))
print(calc_cube(5))
print(calc_cube(-5))
print(string_capitalizer(1))
