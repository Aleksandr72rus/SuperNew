class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec + other.sec)

    def __mul__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec * other.sec)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec - other.sec)

    def __floordiv__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return Clock(self.sec // other.sec)

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec == other.sec

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec < other.sec

    def __le__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec <= other.sec

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных Clock")
        return self.sec >= other.sec

    def __ne__(self, other):
        return not self.__eq__(other)


c1 = Clock(30)
c2 = Clock(200)


print("c1:", c1.get_format_time())
print("c2:", c2.get_format_time())
# c1 += c2

c3 = c1 * c2    #HW
print("c1 * c2:", c3.get_format_time())

c4 = c1 - c2    #HW
print("c1 - c2:", c4.get_format_time())

c5 = c1 + c2    #HW
print("c1 + c2:", c5.get_format_time())


if c1 == c2:
    print("c1 == c2:", "Время одинаково")
else:
    print("c1 != c2:", "Время разное")

if c1 < c2: #HW
    print("c1 < c2:", "Второе время больше")
else:
    print("c1 > c2:", "Первое время больше")

if c1 <= c2: #HW
    print("c1 <= c2:", "Второе время больше или равно первому")
else:
    print("c1 >= c2:", "Первое время больше или равно второму")

if c1 > c2:  # HW
    print("c1 > c2:", "Второе время меньше")
else:
    print("c1 < c2:", "Первое время меньше")

if c1 >= c2:  # HW
    print("c1 >= c2:", "Второе время меньше или равно первому")
else:
    print("c1 <= c2:", "Первое время меньше или равно второму")