# 2. * (вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) для
# получения информации вида: (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>,
#                             <response_size>), например:
#
# raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
# "Debian APT-HTTP/1.3 (0.9.7.9)"'
# parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')
# Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле? Были ли особенные строки?
# Можно ли для них уточнить регулярное выражение?

import re

# Первый вариант с обычным IP адресом
RE_PARSE = re.compile(r"""(?P<IP>(?:\d{1,3}\.){3}\d{1,3})   # парс IP адреса
                            .+
                          (?P<data>\[.+]+)                 # парс даты
                            .+
                          (?:"
                            (?P<type>[A-Z]{2,})             # парс типа запроса
                                \s+
                            (?P<resource>[/\w]+)           # парс ресурса
                                .*?")
                            \s+
                          (?P<code>\d+)                     # парс кода
                            \s+
                          (?P<size>\d+)                     #парс размера
                          """, re.VERBOSE)

# Первый вариант с IP адресом по версии IPv6
RE_PARSE2 = re.compile(r"""(?P<IP>(?:\d{1,3}\.){3}\d{1,3}) |    # парс обычного IP
                           (?:[\da-f]{0,4}:){7}(?:[\da-f]{0,4}) # парс IPv6 адреса (7 двоеточий)
                            .+
                          (?P<data>\[.+]+)                 # парс даты
                            .+
                          (?:"
                            (?P<type>[A-Z]{2,})             # парс типа запроса
                                \s+
                            (?P<resource>[/\w]+)           # парс ресурса
                                .*?")
                            \s+
                          (?P<code>\d+)                     # парс кода
                            \s+
                          (?P<size>\d+)                     #парс размера
                          """, re.VERBOSE)

# Второй вариант с IP адресом по версии IPv6 (оказалось что возможно меньше двоеточий)
RE_PARSE3 = re.compile(r"""(?P<IP>(?:\d{1,3}\.){3}\d{1,3}) |    # парс обычного IP
                           (?:[\da-f]{0,4}:){6,7}(?:[\da-f]{0,4}) # парс IPv6 адреса (6 или 7 двоеточий)
                            .+
                          (?P<data>\[.+]+)                 # парс даты
                            .+
                          (?:"
                            (?P<type>[A-Z]{2,})             # парс типа запроса
                                \s+
                            (?P<resource>[/\w]+)           # парс ресурса
                                .*?")
                            \s+
                          (?P<code>\d+)                     # парс кода
                            \s+
                          (?P<size>\d+)                     #парс размера
                          """, re.VERBOSE)

# Второй вариант с IP адресом по версии IPv6 (оказалось что возможно еще меньше двоеточий)
RE_PARSE4 = re.compile(r"""(?P<IP>(?:\d{1,3}\.){3}\d{1,3}) |    # парс обычного IP
                           (?:[\da-f]{0,4}:){5,7}(?:[\da-f]{0,4}) # парс IPv6 адреса (5 -7 двоеточий)
                            .+
                          (?P<data>\[.+]+)                 # парс даты
                            .+
                          (?:"
                            (?P<type>[A-Z]{2,})             # парс типа запроса
                                \s+
                            (?P<resource>[/\w]+)           # парс ресурса
                                .*?")
                            \s+
                          (?P<code>\d+)                     # парс кода
                            \s+
                          (?P<size>\d+)                     #парс размера
                          """, re.VERBOSE)


url = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"


def download_log_file(url: str, filename="log.txt"):
    """
    Скачивает данные с сервера в файл
    :param url: Ссылка на даные
    :param filename: имя записываемого файла
    :return: тип кодировки файла
    """
    import requests
    response = requests.get(url, stream=True)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    with open(filename, 'wb') as fd:
        for chunk in response.iter_content(chunk_size=1024):
            fd.write(chunk)
    return encodings


def get_file_with_bad_lines(fileName, RE_COMPILE, sourceFile="log.txt"):
    """
    Пытается распарсить файл по скомпелированному шаблону. В случае не нахождения соответсвия,
    записывает строку в файл и выводит ее в консоль
    :param sourceFile: Путь к проверяемому файлу
    :param fileName: Путь к файлу куда пишутся нераспарсенные строки
    :param RE_COMPILE: Скомпелированный шаблон регулярного выражения
    :return: 0 - если все хорошо
    """
    import os.path
    if not os.path.exists(sourceFile):
        enc = download_log_file(url, filename=sourceFile)
    else:
        enc = "UTF-8"

    with open(sourceFile, "rt", encoding=enc) as file, \
            open(fileName, "at", encoding=enc) as file2:
        count = 0
        for line in file:
            temp = RE_COMPILE.match(line)
            try:
                temp.groupdict()
            except AttributeError:
                count += 1
                file2.write(line)
                print(line.strip())
        print(count)
        print()
    return 0


get_file_with_bad_lines("easyVarIP.txt", RE_PARSE)
get_file_with_bad_lines("VarIPv6.txt", RE_PARSE2)
get_file_with_bad_lines("VarIPv6_ver2.txt", RE_PARSE3)
get_file_with_bad_lines("VarIPv6_ver3.txt", RE_PARSE4)
