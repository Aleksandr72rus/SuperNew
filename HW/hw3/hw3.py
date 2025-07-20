penny = int(input("Введите число копеек от 1 до 99: "))
remains = penny
if 11 <= penny <= 14:
    print(penny, "копеек")
elif 1 <= penny <= 99:
    remains = remains % 10
    if remains == 1:
        print(penny, "копейка")
    elif 2 <= remains <= 4:
        print(penny, "копейки")
    else:
        print(penny, "копеек")
else:
    print("Некорректное число")
