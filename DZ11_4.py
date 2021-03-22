# 4. Реализовать проект «Операции с комплексными числами».
#
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self):
        if self.im > 0:
            return f"{self.re}+i{self.im}"
        else:
            return f"{self.re}-i{abs(self.im)}"

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self.re + other, self.im)
        try:
            return ComplexNumber(self.re + other.re, self.im + other.im)
        except AttributeError:
            raise ValueError(f"Нельзя сложить {type(self)}:{str(self)} и {type(other)}:{str(other)}")

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self.re - other, self.im)
        try:
            return ComplexNumber(self.re-other.re, self.im-other.im)
        except AttributeError:
            raise ValueError(f"Нельзя вычесть {type(self)}{str(self)} и {type(other)}{str(other)}")

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = ComplexNumber(other, 0)
        try:
            return ComplexNumber(self.re*other.re - self.im*other.im, self.re*other.im + self.im*other.re)
        except Exception:
            raise ValueError(f"Нельзя умножить {type(self)}{str(self)} и {type(other)}{str(other)}")

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            other = ComplexNumber(other, 0)
        try:
            a1, a2 = self.re, other.re
            b1, b2 = self.im, other.im
            return ComplexNumber((a1*a2 + b1*b2)/(a2**2 + b2**2), (a2*b1 + a1*b2) / (a2**2 + b2**2))
        except Exception:
            raise ValueError(f"Нельзя поделить {type(self)}{str(self)} и {type(other)}{str(other)}")


c1 = ComplexNumber(3, 1)
c2 = ComplexNumber(5, -2)


print(c1)
print(c2)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1 + 5)
print(c1 - 5)
print(c1 * 5)
print(c1 / 5)

