import math

area = {
    'Circle': lambda r: math.pi * (r ** 2),
    'Rectangle': lambda a, b: a * b,
    'Trapezoid': lambda a, b, h: (a + b) * h * 0.5,
}

print("Площадь окружности радиуса 2: ", area['Circle'](2))
print("Площадь прямоугольника размером 10*13: ", area['Rectangle'](10, 13))
print("Площадь трапеции для a=7, b=5, h=3: ", area['Trapezoid'](7, 5, 3))

