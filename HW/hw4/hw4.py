count = input("Укажите кол-во символов: ")
while type(count) is not int:
    try:
        count = int(count)
    except ValueError:
        print("Введите целое число")
        count = input("Введите целое число: ")

types = input("Укажите Вид символа: ")
orient = input("Укажите направление, 0 - по вертикале, 1 -по горизонтали: ")

i = 0

while i <= count:
    if orient == 1:
        print(types, end=" ")
    if orient == 0:
        print(types, end="\n")
    i += 1
    while type(orient) is not int:
        i = 0
        try:
            orient = int(orient)
            if orient == 0 or orient == 1:
                pass
            else:
                print("Неверное направление!")
                orient = input("Введите направление 1 или 0: ")
        except ValueError:
            print("Неверное направление!")
            orient = input("Введите направление 1 или 0: ")
        i += 1




