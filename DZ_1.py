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
    return dictionary.get(str_number)


print(num_translate("two"))
