from random import randint


def completion(first, finish):
    return tuple(randint(first, finish) for i in range(10))


tpl1 = completion(0, 5)
tpl2 = completion(-5, 0)
tpl_end = tpl1 + tpl2

print(tpl1)
print(tpl2)
print(tpl_end)
print("0 = ", tpl_end.count(0))
