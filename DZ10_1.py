# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |

class Matrix:
    def __init__(self, data):
        temp = len(data[0])
        for row, line in enumerate(data):
            if not isinstance(line, list) or len(line) != temp:
                raise TypeError("Строки в матрице разной длинны")
            for col, element in enumerate(line):
                try:
                    if isinstance(element, int):
                        continue
                    line[col] = float(element)
                except ValueError:
                    raise ValueError(f"Элемент матрицы [{row+1}][{col+1}] - не вещественное число")
        self.data = data

    def __str__(self):
        temp = ""
        for line in self.data:
            temp += "| "
            for element in line:
                temp += f"{element} "
            temp += "|\n"
        return temp


l1 = [[1,2,3],[2,3,4],[3,4,5]]
# l2 = [[1,2,3],[2,3],[3,4]]
l3 = [[1,2,3],[2,"3",4],[3,4,5]]


m1 = Matrix(l1)
m2 = Matrix(l3)
print(m2)

