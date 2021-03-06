import itertools
import json


def function_with_good_name(user_file="users.csv", hobby_file="hobby.csv"):
    """
    Объединяет людей с их увлечениями,
    Сереализует результат в json
    P.S. Попробовал сделать так чтобы файлы все таки не читались целиком
    :param user_file: Файл с именами
    :param hobby_file: Файл с увлечениями
    :return: 0 - если все хорошо, 1 - если записи с именами кончились
    """
    with open(user_file, "rt", encoding="UTF-8")as user_file, \
            open(hobby_file, "rt", encoding="UTF-8") as hobby_file:
        result = {}
        res_code = 0
        for line in itertools.zip_longest(user_file, hobby_file):
            if line[0] is not None:
                name = line[0].strip().replace(",", " ")
                if name == "":
                    break
            else:
                res_code = 1
                break
            hobby = line[1].strip().split(",") if line[1] is not None else None
            if hobby == [""]:
                hobby = None
            result[name] = hobby
    with open("result_users_hobby,json", "w", encoding="UTF-8") as file:
        json.dump(result, file)
    return res_code


function_with_good_name()
with open("result_users_hobby,json", "r", encoding="UTF-8") as file:
    res = json.load(file)
print(res)
