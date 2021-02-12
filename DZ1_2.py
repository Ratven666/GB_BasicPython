for i in range(1, 1000, 2):
    number = i ** 3
    summa = 0
    j = 1
    while True:
        temp = number % 10**j // 10**(j-1)
        summa += temp
        if number // 10**(j-1) == 0:
            break
        j += 1
    if summa % 7 == 0:
        print("число:", number, "sum:", summa)

