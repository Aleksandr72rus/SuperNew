
len_str = len(open("str.txt", "r").readlines())
with open("str.txt", "r") as f:
    print(f.read())
pos1 = int(input("pos1 = "))
pos2 = int(input("pos2 = "))

if 0 <= pos1 <= len_str and 0 <= pos2 < len_str:
    with open("str.txt") as f:
        read_line = f.readlines()
        read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]

    with open("str.txt", "w") as f:
        f.writelines(read_line)

    with open("str.txt", "r") as f:
        print(f.read())

else:
    print("Ошибка ввода! Введите строки, которые нужно заменить!")

