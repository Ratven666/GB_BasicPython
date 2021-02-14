duration = int(input("Введите время в секундах: "))

days = duration // (24 * (60**2))
duration -= days * (24 * (60**2))
hours = duration // 60 ** 2
duration -= hours * 60 ** 2
minutes = duration // 60
seconds = duration % 60

if days != 0:
    print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
elif hours != 0:
    print(hours, "час", minutes, "мин", seconds, "сек")
elif minutes != 0:
    print(minutes, "мин", seconds, "сек")
else:
    print(seconds, "сек")