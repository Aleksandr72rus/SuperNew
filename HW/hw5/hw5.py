
# i = 0
# num = [int(input("-> ")) for _ in range(int(input("n = ")))]
# print(num)
# sum1 = 0
# while (i < len(num)
#     if num[i] < 0):
#         sum1 += num[i]
#         i += 1
#
# print("Сумма отрицательных чисел: ", sum1)

# 2 variant
# num = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(num)
# sum1 = 0
#
# for i in num:
#     if i < 0:
#         sum1 += i
# print("Сумма отрицательных чисел: ", sum1)

# 3 variant
# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных чисел: ", s)

#4 variant

a = [int(input("-> ")) for i in range(int(input("n = ")))]
s = 0
for i in a:
    if i < 0:
        s += 1
print("Сумма отрицательных чисел: ", s)

