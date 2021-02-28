src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56]


def check_max_in_pair_gen(data: list):
    """
    Выводит элементы списка, значения которых больше предыдущего (первое число не выводится)
    :param data: Список чисел
    :return: Число, если оно больше предыдущего
    """
    for index, el in enumerate(data):
        if index == len(data) - 1:
            break
        if data[index] < data[index+1]:
            yield data[index+1]


gen = check_max_in_pair_gen(src)
for i in gen:
    print(i)
