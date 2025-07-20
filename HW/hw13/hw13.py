study = {}

length = int(input("Количество студентов: "))
sum_score = 0

for element in range(0, length):
    name = input(str(element + 1) + "-й студент: ")
    score = int(input("Балл: "))
    study[name] = score
    sum_score += score

gpa = sum_score / length

print("Все студенты: ", *study)
print("Средний балл: ", gpa, "\nСтуденты выше среднего балла: ")

for point in study:
    if study[point] > gpa:
        print(point)
