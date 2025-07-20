from math import pi, sqrt

print(" Вычисление площади фигур\n\n" "Выбор фигуры: ")
form = int(input("1 - Треугольник\n" "2 - Прямоугольник\n" "3 - Круг\n" ": "))
print(form)

while 1 <= form <= 3:
    if form == 1:
        tri = [int(input("Введите сторону треугольника: ")) for _ in range(3)]
        p = sum(tri)/2
        print(p)
        s_tri = sqrt(p*(p - tri[0])*(p - tri[1])*(p - tri[2]))
        print("Площадь треугольника: ", s_tri)
        break
    if form == 2:
        rect = [int(input("Введите длину, затем ширину прямоугольника: ")) for _ in range(2)]
        s_rect = rect[0] * rect[1]
        print("Площадь прямоугольника: ", s_rect)
        break
    if form == 3:
        circle = [int(input("Введите радиус круга: ")) for _ in range(1)]
        s_circle = 2 * pi * circle[0] ** 2
        print("Площадь круга: ", s_circle)
        break
else:
    print(" Вы наверно устали?\n Будьте внимательнее!\n Выберите фигуру цифрой от 1 до 3!")
