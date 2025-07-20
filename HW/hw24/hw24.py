class Car:

    def __init__(self, model, year, author, power, color, price):
        self.model = model
        self.year = year
        self.author = author
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}")
        print(f"Год выпуска: {self.year}")
        print(f"Производитель: {self.author}")
        print(f"Мощность двинателя: {self.power}")
        print(f"Цвет машины: {self.color}")
        print(f"Цена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_author(self, author):
        self.author = author

    def set_power(self, power):
        self.power = power

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

    def get_model(self, model):
        return self.model

    def get_year(self, year):
        return self.year

    def get_author(self, author):
        return self.author

    def set_power(self, power):
        return self.power

    def get_color(self, color):
        return self.color

    def get_price(self, price):
        return self.price


c1 = Car("X3", "2020", "BMW", "160", "Black", "5600000")
c1.print_info()

