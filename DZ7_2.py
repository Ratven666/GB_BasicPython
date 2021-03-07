import yaml
import os.path

# with open("config.yaml", "rt", encoding="UTF-8") as file:
#     config = []
#     for line in file:
#         config.append(line)

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)


def create_dir(directory: dict):
    """
    Рекурсивно создает структуру директорий и файлов из словаря,
    где ключ - имя директории, значения - содержимое директории
    :param directory: словарь с требуемой структурой директорий-файлов
    :return: 0 - если все хорошо
    """
    for k, v in directory.items():
        if not os.path.exists(k):
            os.mkdir(k)
        os.chdir(k)
        for el in v:
            if type(el) is dict:
                create_dir(el)
            if type(el) is str:
                with open(el, "a"):
                    pass
        os.chdir("..")
        return 0


create_dir(config)
