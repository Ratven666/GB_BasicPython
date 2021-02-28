def iterator_without_yield(n: int):
    """
    Генератор нечётных чисел от 1 до n (включительно), без использования ключевого слова yield,
    для чисел, квадрат которых меньше 200.
    """
    return (el for el in range(1, n+1, 2) if el**2 < 200)


gen = iterator_without_yield(20)

for i in gen:
    print(i)

print(next(gen))
