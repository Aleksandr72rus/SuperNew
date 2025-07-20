# 3547


a = lst = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
new_lst = []
i = 0
for element in lst:
    k = element
    for j in lst:
        if k == j:
            i += 1
    if i == 1:
        # print(k, end=" ")
        new_lst.append(k)
    i = 0

print(new_lst)


for i in a:
    if a.count(i) == 1:
        print(i, end=" ")



