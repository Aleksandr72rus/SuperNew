import random

lst = [random.randint(0, 100) for i in range(10)]
print(lst)

lst_new = lst.copy()
new_lst = sorted(lst)
min_val = new_lst[0]

# print(new_lst)
print("Минимальный элемент:", min_val)

ind = lst_new.index(min_val)
print("Индекс минимального эл-та: ", ind)
del lst[:ind]
print(lst)


