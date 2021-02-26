src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]


def ordered_unic_list(data: list):
    """
    Возвращает список элементов переданного списка не имеющих повтороний
    с сохранением порядка их следования
    :param data: список чисел
    :return: список чисел не имеющих повторений в исходном порядке
    """
    counter = {}
    for elem in data:
        counter[elem] = counter.get(elem, 0) + 1
    return [el for el in data if counter[el] == 1]


print(ordered_unic_list(src))
"""
Так до конца и не понял причем тут генераторы(
если честно, не могу придумать как проще и быстрее сделать...
"""
