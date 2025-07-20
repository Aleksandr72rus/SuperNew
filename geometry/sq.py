class Square:
    def __init__(self, a):
        self.a = a

    def perimetr(self):
        return 4 * self.a


s1 = Square(10)
s2 = Square(20)

if __name__ == "__main__":
    print(s1.perimetr())
    print(s2.perimetr())