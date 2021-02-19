def thesaurus(*args: str) -> dict:
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