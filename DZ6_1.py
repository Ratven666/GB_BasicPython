import requests
import os.path
url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"


def download_log_file(url: str, filename="log.txt"):
    """
    Скачивает данные с сервера в файл
    :param url: Ссылка на даные
    :param filename: имя записываемого файла
    :return: тип кодировки файла
    """
    response = requests.get(url, stream=True)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=1024):
            fd.write(chunk)
    return encodings


def parse_logfile(filename="log.txt", encoding="UTF-8"):
    """
    Парсит построчно данные из файла, проверяя структуру строки
    :param filename: Имя файла с данными
    :param encoding: Тип кодировки файла
    :return: список кортежей по заданию
    """
    res_list = []
    with open(filename, "rt", encoding=encoding) as file:
        check_set = set()
        count = 0
        for line in file:
            temp = line.strip().split("\"")
            count += 1
            check_set.add(len(temp))
            if len(check_set) > 1:
                print(f"Что-то не так с {count} строкой")
                continue
            res_list.append((temp[0].split()[0], temp[1].split()[0], temp[1].split()[1]))
    return res_list


def get_res_tuple():
    """
    Просто метод проверяющий наличие файла и скачивающий его при необходимости
    :return: список кортежей по заданию
    """
    if not os.path.exists("log.txt"):
        enc = download_log_file(url)
    else:
        enc = "UTF-8"
    return parse_logfile("log.txt", enc)


if __name__ == "__main__":
    res = get_res_tuple()

    # for el in res:
    #     print(el)

