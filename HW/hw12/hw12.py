sales = {
    "John": {
        "N": 3056,
        "S": 8463,
        "E": 8441,
        "W": 2694
    },
    "Tom": {
        "N": 4832,
        "S": 6786,
        "E": 4737,
        "W": 3612
    },
    "Anne": {
        "N": 5239,
        "S": 4802,
        "E": 5820,
        "W": 1859
    },
    "Fiona": {
        "N": 3904,
        "S": 3645,
        "E": 8821,
        "W": 2451
    }
}

for name in sales:
    print(name)
    for indicator in sales[name]:
        print("\t", indicator, ":", sales[name][indicator])

for name in sales:
    n = input("Имя: ")
    s = input("Регион: ")
    print(sales[n][s])
    new_ind = input("Новое значение: ")
    sales[n][s] = new_ind
    print(sales[n])
    break









