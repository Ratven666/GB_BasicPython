def thesaurus(*args: str) -> dict:
    """
    Функция возвращает отсортированный по алфавиту словарь с именами, где ключи - первые буквы имен

    :param args: набор имен сортируемых в словарь
    :return: словарь с именами
    """
    name_list = sorted(list(args))
    result = {}
    for name in name_list:
        if name[0] in result.keys():
            result[name[0]].append(name)
        else:
            result[name[0]] = []
            result[name[0]].append(name)
    return result


a = thesaurus("Иван", "Мария", "Петр", "Илья")
print(a)
print(thesaurus.__doc__)