num = int(input("Введите пятизначное число: "))
# print(num)

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
num = num // 10
d = num % 10
num = num // 10
e = num % 10
summa = a+b+c+d+e
print("Сумма чисел: ", summa)
print("Среднее арифметическое: ", summa / 5)
