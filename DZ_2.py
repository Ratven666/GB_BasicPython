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


def num_translate_adv(str_number: str, dictionary: dict = eng_rus_dict) -> str:
    """
    Переводит числительные от 1 до 10 на русский язык с учетом регистра первой буквы

    :str_number: числительное, требующее перевода
    :dictionary: словарь с переводом (по умолчанию - английский)
    :return: str с переводом
    """

    if str_number[0].isupper():
        return dictionary.get(str_number.lower()).capitalize()
    return dictionary.get(str_number)


print(num_translate_adv("one"))
print(num_translate_adv("One"))
print(num_translate_adv("Two"))
print(num_translate_adv("six"))
print(num_translate_adv("Quatre", france_rus_dict))

print(num_translate_adv.__doc__)
