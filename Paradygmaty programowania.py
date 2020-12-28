#programowanie proceduralne
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

rock = []
country = []
def collect_songs():
    song = "Wpisz tytul piosenki: "
    ask = "wcisnij r, c albo q aby wyjsc: "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == ("c"):
            co = input(song)
            country.append(co)

        else:
            print("Nieprawidłowe polecenie")

    print(country)
    print(rock)

collect_songs()

#programowanie funkcyjne

def inkrementacja(a):
    return a + 1

print(inkrementacja(2))

class Orange:
    def __init__(self,w ,c):
        self.weight = w
        self.color = c
        print("Utowrzono")

or1 = Orange(280, "Ciemnopomaranczowe")
print(or1)
print(or1.weight)
print(or1.color)

or1.weight = 300
or1.color = "Zielony"
print(or1)
print(or1.weight)
print(or1.color)

or2 = Orange(420, "Czerwony")
or3 = Orange(450, "Fioletowy")
print(or2)
print(or3)

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

pp = Rectangle(10, 2)
print(pp.area())

class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} na {}".format(self.width, self.len))

prostok = Shape(10, 20)
prostok.print_size()

class square(Shape):
    pass

kwadrat = square(10, 10)
kwadrat.print_size()


