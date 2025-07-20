
def my_decorator(func):
    def wrap(*args):
        st = ""
        for i in args:
            st += str(i) + ", "
        print("Среднее арифметическое чисел: ", st[:-2], "=",  func(*args) / len(args))
    return wrap


@my_decorator
def return_num(*args):
    print("Сумма чисел: ", *args, "=", sum(args))
    return sum(args)


return_num(2, 3, 3, 4)

#
#
#

# tpl = [int(input("-> ")) for i in range(int(input("Введите кол-во элементов списка: ")))]
# print("Полученные числа: ", *tpl)
#
#
# def my_decorator(func):
#     def wrap():
#         return func() / len(tpl)
#     return wrap
#
#
# @my_decorator
# def return_num():
#     return sum(tpl)
#
#
# print("Сумма чисел ", *tpl, "=", sum(tpl))
# print("Среднее арифметическое чисел ", *tpl, "=", return_num())
