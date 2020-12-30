class Rectagle():
    def __init__(self, w, l):
        self.wysokosc = w
        self.dlugosc = l

    def area(self):
        return self.dlugosc * self.wysokosc

prostok = Rectagle(8, 2)
print(prostok.area())

class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)

class Shape():
    def __init__(self, w, l):
        self.dlugosc = l
        self.szerokosc = w

    def print_size(self):
        print("{} na {}".format(self.dlugosc, self.szerokosc))

kwadrat = Shape(20, 10)
kwadrat.print_size()

class Square(Shape):
    def area(self):
        print("Pole kwadratu to: ")
        return self.dlugosc * self.szerokosc

    def square_size(self):
        print("Wymiary kwadratu to: {} na {}".format(self.dlugosc, self.szerokosc))

s_square = Square(10, 10)
s_square.print_size()
print(s_square.area())
s_square.square_size()

class Dog():
    def __init__(self, i, r, w):
        self.imie = i
        self.rasa = r
        self.wlasciciel = w

class Person():
    def __init__(self, i):
        self.imie = i

jan = Person("Jan")
szalik = Dog("szalik", "buldog", jan)
print(szalik.wlasciciel.imie)




