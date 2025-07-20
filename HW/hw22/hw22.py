import os
import time

file = r"D:\Python\HW\hw22\4.txt"


def print_tree():
    if os.path.isfile(file):
        print("4.txt", os.path.join(file), "-", "last access time ", os.path.getatime(file))
    else:
        print("Такого пути не существует!")


print_tree()
