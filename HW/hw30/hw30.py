import math
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, a, color):
        super().__init__(color)
        self.a = a

    def perimeter(self):
        return self.a * 4

    def area(self):
        return self.a * self.a

    def draw(self):
        return ("*  " * self.a + "\n") * self.a

    def info(self):
        print(f"=== Квадрат ===\nСторона: {self.a}\nЦвет: {self.color}"
              f"\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n{self.draw()}\n")


class Rectangle(Shape):
    def __init__(self, w, h, color):
        super().__init__(color)
        self.w = w
        self.h = h

    def perimeter(self):
        return (self.w + self.h) * 2

    def area(self):
        return self.w * self.h

    def draw(self):
        return ("* " * self.h + "\n") * self.w

    def info(self):
        print(f"=== Прямоугольник ===\nДлина: {self.w}\nШирина: {self.h}\nЦвет: {self.color}"
              f"\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n{self.draw()}\n")


class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        p = self.perimeter() / 2
        return round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)

    def draw(self):
        st = []
        for n in range(self.b):
            st.append(" " * n + "*" * (self.a - 2 * n))
        # st.reverse()
        return "\n".join(reversed(st))

    def info(self):
        print(f"=== Треугольник ===\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}"
              f"\nЦвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n{self.draw()}\n")


sq = Square(3, "red")
rect = Rectangle(3, 7, "green")
tr = Triangle(11, 6, 6, "yellow")

total = [sq, rect, tr]

for g in total:
    g.info()
