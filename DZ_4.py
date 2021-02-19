def thesaurus_adv(*args: str) -> dict:
    name_list = list(args)
    result = {}
    for name in name_list:
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
    for key in sorted(result.keys()):
        temp[key] = result[key]
    result = temp
    return result


a = thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
                  "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков")
print(a)