class Student:

    def __init__(self):
        self.name1 = "Roman"
        self.name2 = "Vladimir"
        self.cpu1 = self.CPURoman()
        self.cpu2 = self.CPUVladimir()

    def print_roman(self):
        print(f"{self.name1} => {cpu_roman.cpu()}, {cpu_roman.model()}, {cpu_roman.memory()}")

    def print_vladimir(self):
        print(f"{self.name2} => {cpu_vladimir.cpu()}, {cpu_vladimir.model()}, {cpu_vladimir.memory()}")

    class CPURoman:
        @staticmethod
        def cpu():
            return "HP"

        @staticmethod
        def model():
            return "Core-i7"

        @staticmethod
        def memory():
            return "16 Gb"

    class CPUVladimir:
        @staticmethod
        def cpu():
            return "HP"

        @staticmethod
        def model():
            return "Core-i7"

        @staticmethod
        def memory():
            return "16 Gb"


study = Student()
cpu_roman = study.CPURoman
cpu_vladimir = study.CPUVladimir
study.print_roman()
study.print_vladimir()
