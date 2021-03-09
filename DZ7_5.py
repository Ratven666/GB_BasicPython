import os
import json


target_dir = "C:\\Users\\Mikhail Vystrchil\\Downloads"


def show_dir_stat(directory: str):
    """
    Метод который выводит статистику для заданной папки в виде словаря,
    в котором ключи — верхняя граница размера файла (кратна 10), а значения - список из количества таких файлов,
    и списка расширений файлов (если у файла нет расширения выводится "!not_def!").
    Также сериализует полученный словарь в json файл с именем: "<folder_name>_summary.json"
    :param directory: Директория для которой выполняется проверка
    :return: 0 - если все хорошо, 1 - если передана не директория
    """
    if not os.path.isdir(directory):
        print("Передана не директория!")
        return 1

    result = {}
    for path, dirs, files in os.walk(directory):
        for file in files:
            i = 1
            temp_path = os.path.join(path, file)
            while True:
                key = 10 ** i
                if os.path.getsize(temp_path) < key:
                    result[key] = result.get(key, [0, set()])
                    result[key][0] += 1
                    temp = file.split(".")
                    if len(temp) > 1 and not file.startswith("."):
                        result[key][1].add(temp[-1])
                    else:
                        result[key][1].add("!not_def!")
                    break
                i += 1

    for k in sorted(result.keys()):
        result[k][1] = list(result[k][1])
        print(k, result[k], sep=" : ")

    path = os.path.join(os.path.abspath("."), os.path.basename(target_dir))
    path += "_summary.json"
    with open(path, "w") as file:
        json.dump(result, file, indent=4)
    return 0


show_dir_stat(target_dir)
