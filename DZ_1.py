eng_rus_dict = {"one": "один",
                "two": "два",
                "three": "три",
                "four": "четыре",
                "five": "пять",
                "six": "шесть",
                "seven": "семь",
                "eight": "восемь",
                "nine": "девять",
                "ten": "десять"}

france_rus_dict = {"un": "один",
                   "deux": "два",
                   "trois": "три",
                   "quatre": "четыре",
                   "cinq": "пять",
                   "six": "шесть",
                   "sept": "семь",
                   "huit": "восемь",
                   "neuf": "девять",
                   "dix": "десять"}


def num_translate(str_number: str, dictionary: dict = eng_rus_dict) -> str:
    """
    Переводит числительные от 1 до 10 на русский язык

    :str_number: числительное, требующее перевода
    :dictionary: словарь с переводом (по умолчанию - английский)
    :return: str с переводом
    """
    return dictionary.get(str_number)


print(num_translate("two"))

print(num_translate.__doc__)
