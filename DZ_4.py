def thesaurus_adv(*args: str) -> dict:
    """
    Функция принимающая в качестве аргументов строки в формате «Имя Фамилия» и возвращающая словарь,
    в котором ключи — первые буквы фамилий, а значения — словари с именами, где ключи - первые буквы имен

    :param args: набор строк "Имя Фамилия" сортируемых в словари
    """
    result = {}
    for name in args:
        name_list = name.split(" ")
        if name_list[1][0] in result.keys():
            result[name_list[1][0]].append(name)
        else:
            result[name_list[1][0]] = []
            result[name_list[1][0]].append(name)
    for key, value in result.items():
        temp = {}
        if len(value) == 1:
            continue
        for name in sorted(value):
            name_list = name.split(" ")
            if name_list[0][0] in temp.keys():
                temp[name_list[0][0]].append(name)
            else:
                temp[name_list[0][0]] = []
                temp[name_list[0][0]].append(name)
        result[key] = temp
    temp.clear()
    for key in sorted(result.keys()):
        temp[key] = result[key]
    result = temp
    return result


a = thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
                  "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
print(a)
print(thesaurus_adv.__doc__)