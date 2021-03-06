def main(argv):
    """
    Выводит в консоль данные из файла с продажами
    :param argv: параметры из консоли
    :return: 0 - если все хорошо, 1 - если параметры не числа, 2 - если параметров больше двух
    """
    program, *args = argv
    if len(args) == 0:
        with open("bakery.csv", "rt", encoding="UTF-8") as file:
            for line in file:
                print(line.strip())
        return 0

    if len(args) == 1:
        try:
            index = int(args[0])
        except ValueError:
            print("Параметр должен быть целым числом!")
            return 1
        with open("bakery.csv", "rt", encoding="UTF-8") as file:
            counter = 1
            for line in file:
                if counter >= index:
                    print(line.strip())
                counter += 1
        return 0

    if len(args) == 2:
        try:
            start_index = int(args[0])
            end_index = int(args[1])
        except ValueError:
            print("Параметры должны быть целыми числами!")
            return 1
        with open("bakery.csv", "rt", encoding="UTF-8") as file:
            counter = 1
            for line in file:
                if start_index <= counter <= end_index:
                    print(line.strip())
                counter += 1
                if counter > end_index:
                    return 0
        return 0
    return 2


if __name__ == "__main__":
    import sys
    exit(main(sys.argv))
