import os.path

def main(argv):
    """
    Костыльный скрипт который редактирует нужные записи исходя из того что длина строки заранее известна

    Проверка существования строки работает через сравнение размера файла и ожидаемого индекса редактируемой строки

    :param argv: Параметры из консоли
    :return: 0 - если все хорошо, 1 - если параметров меньше или больше двух, или они не числа,
    2 - если нет строки с таким номером
    """
    program, *args = argv
    if len(args) != 2:
        return 1
    try:
        index = int(args[0])
        value = str(int(args[1]))
    except ValueError:
        print("Параметры должны быть числами!")
        return 1
    with open("bakery.csv", "r+") as file:
        st_index = 17 * (index-1)
        file.seek(st_index)
        if st_index > os.path.getsize("bakery.csv"):
            print("Записи под таким номером нет!")
            return 2
        file.write(value + "\b"*(15-len(value)))
    return 0


if __name__ == "__main__":
    import sys
    exit(main(sys.argv))
