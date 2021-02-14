"""
4. Создать список, содержащий цены на товары (10 – 20 товаров), например:
[57.8, 46.51, 97, ...]
- Вывести на экран эти цены через запятую в одну строку,
цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

- Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать,
что объект списка после сортировки остался тот же).
- Создать новый список, содержащий те же цены, но отсортированные по убыванию.
- Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
"""

import random
data = []
for i in range(random.randint(10, 20)):
    data.append(round(random.random() * 100, 2))

print(data)

def get_result_string(data):
    result_string = ""
    for element in data:
        s = str(element).split(".")
        for index, element in enumerate(s):
            temp = element
            if len(element) == 1 and index != 0:
                temp = f"0{element}"
            if index == 0:
                result_string += f"{temp} руб "
            if index == 1:
                result_string += f"{temp} коп, "
    return result_string

print("\nВывод строки по заданию:")
print(get_result_string(data))

print("\nid до соритровки по возрастанию: ", id(data))
data.sort()
print(get_result_string(data))
print("id после соритровки по возрастанию: ", id(data))

import copy
new_list = copy.copy(data)
new_list.reverse()

print("\nid нового списка после соритровки по убыванию: ", id(new_list))
print(new_list)
print("5 самых дорогих товаров:")
print(get_result_string(new_list[0:5]))
