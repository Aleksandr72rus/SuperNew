

def find_negative(numb):
    if len(numb) == 0:
        return 0
    temp = 0
    if numb[0] < 0:
        temp += 1
    return temp + find_negative(numb[1:])


print(find_negative([-2, 3, 8, -11, -4, 6]))
