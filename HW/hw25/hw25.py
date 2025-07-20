import math


class Square:
    __count = 0

    @staticmethod
    def geron_area(a, b, c):
        p = (a + b + c) / 2
        s = math.sqrt(p * (p - a) * (p - b) * (p - c))
        Square.__count += 1
        return s

    @staticmethod
    def triangle_area(a, h):
        s = (a * h) / 2
        Square.__count += 1
        return s

    @staticmethod
    def square_area(a):
        s = a ** 2
        Square.__count += 1
        return s

    @staticmethod
    def rectangle_area(a, b):
        s = a * b
        Square.__count += 1
        return s

    @staticmethod
    def get_count():
        return Square.__count


print("Площадь треугольника по формуле Герона:", Square.geron_area(3, 4, 5))
print("Площадь треугольника через основание и высоту:", Square.triangle_area(6, 7))
print("Площадь квадрата:", Square.square_area(7))
print("Площадь прямоугольника:", Square.rectangle_area(2, 6))
print("Количество подсчетов площади:", Square.get_count())
