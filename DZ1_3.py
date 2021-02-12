for i in range(21):
    if i % 10 == 1 and i % 100 != 11:
        print(i, "процент")
    elif 2 <= i % 10 <= 4 and (i % 100 < 12 or i % 100 > 14):
        print(i, "процента")
    else:
        print(i, "процентов")


