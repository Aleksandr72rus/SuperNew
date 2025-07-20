import csv
# 1ый вариант
with open("data2.csv", "r") as f:
    file_reader = csv.reader(f, delimiter=";")
    for row in file_reader:
        print(row)
print()
# 2 вариант
with open("data2.csv", "r") as f:
    file_reader = csv.DictReader(f, delimiter=";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f"Файл содержит столбцы: {', '.join(row)}")
        print(f"\thostname: {row['hostname']}\tvendor: {row['vendor']}\tmodel: {row['model']}\tlocation: {row['location']}")
        count += 1