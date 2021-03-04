def main(argv):
    """
    Без особых затей добавляет продажи в файл
    P.S. если параметров несколько до добавляет их все,
    если передано не число, то в консоль будет выведено сообщение о ошибке,
    остальное - добавится
    :param argv: параметры из консоли
    :return: 0 - если все хорошо, 1 - если параметры не переданы
    """
    program, *args = argv
    if len(args) == 0:
        return 1
    with open("bakery.csv", "at", encoding="UTF-8") as file:
        for index, val in enumerate(args):
            try:
                val = int(val)
            except ValueError:
                print(f"В параметре {index + 1} что-то не то...")
                continue
            file.write(str(val))
            file.write("\n")
    return 0


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
