# ////////////// 1 Var (Property)

class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.__num} принадлежащий {self.__surname} был закрыт")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @property
    def chang_num(self):
        return self.__num

    @chang_num.setter
    def chang_num(self, n):
        if isinstance(n, int):
            self.__num = n
        else:
            raise TypeError("Значение должно быть числом!")

    @property
    def chang_name(self):
        return self.__surname

    @chang_name.setter
    def chang_name(self, sn):
        if  isinstance(sn, str):
            self.__surname = sn
        else:
            raise TypeError("Значение должно быть строкой!")

    @property
    def chang_val(self):
        return self.__value

    @chang_val.setter
    def chang_val(self, val):
        if isinstance(val, int):
            self.__value = val
        else:
            raise TypeError("Значение должно быть числом!")

    @property
    def chang_perc(self):
        return self.__value

    @chang_perc.setter
    def chang_perc(self, pr):
        if isinstance(pr, float):
            self.__percent = pr
        else:
            raise TypeError("Значение должно быть вещественным числом!")

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.__value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.__value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.__num}")
        print(f"Владелец: {self.__surname}")
        self.print_balance()
        print(f"Проценты: {self.__percent:.0%}")
        print("-" * 20)

    def edit_owner(self, surname):
        self.__surname = surname

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.__value -= val
            print(f"{val} {Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.chang_num = 789123

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")

acc.chang_name = "Лермонтов"

acc.print_info()
print()

acc.chang_perc = 0.5

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.chang_val = 10000

acc.withdraw_money(3000)
print()
print()
print()
print()

# ////////////// 2 Var (Get/Set)


class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, num, surname, percent, value):
        self.num = num
        self.surname = surname
        self.percent = percent
        self.value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} был открыт")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    def set_chang_val(self, val):
        if isinstance(val, int):
            self.value = val
        else:
            raise TypeError("Значение должно быть числом!")

    def set_chang_num(self, n):
        if isinstance(n, int):
            self.num = n
        else:
            raise TypeError("Значение должно быть числом!")

    def set_chang_name(self, sn):
        if isinstance(sn, str):
            self.surname = sn
        else:
            raise TypeError("Значение должно быть строкой!")

    def set_chang_perc(self, pr):
        if isinstance(pr, int):
            self.percent = pr
        else:
            raise TypeError("Значение должно быть числом!")

    def get_chang_val(self):
        return self.value

    def get_chang_num(self):
        return self.num

    def get_chang_name(self):
        return self.surname

    def get_chang_perc(self):
        return self.value

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете: ")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец: {self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)

    def edit_owner(self, surname):
        self.surname = surname

    def add_percents(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято")
        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()


acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_balance()
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()

acc.set_chang_num(555555)

Account.set_usd_rate(2)
acc.convert_to_usd()
Account.set_eur_rate(3)
acc.convert_to_eur()
print()

acc.edit_owner("Дюма")

acc.set_chang_name("Гоголь")

acc.print_info()
print()

acc.add_percents()
print()

acc.withdraw_money(100)
print()

acc.withdraw_money(3000)
print()

acc.add_money(5000)
print()

acc.withdraw_money(3000)
print()



