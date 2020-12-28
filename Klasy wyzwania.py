import math
class Aplle():
    def __init__(self, ko, dn, kr, wag):
        self.koszt = ko
        self.dni = dn
        self.kraj = kr
        self.waga = wag

jablko = Aplle(2.50, 40, "Polska", 340)
print(jablko.dni)
print(jablko.koszt)
print(jablko.kraj)
print(jablko.waga)

class Circle():
    def __init__(self, r):
        self.promien = r
        self.promien_do_kw = r**2

    def area(self):
        return math.sqrt(self.promien_do_kw)

kolo = Circle(3)
print(kolo.promien_do_kw)
print(kolo.area())

class Triangle():
    def __init__(self, w, p):
        self.wysokosc = w
        self.podstawa = p

    def pole(self):
        return (self.podstawa * self.wysokosc)/2

tr = Triangle(3, 4)
print(tr.pole())

class Hexagon():
    def __init__(self, d):
        self.dlugos_boku = d

    def calculate_perimeter(self):
        return self.dlugos_boku * 6

sze = Hexagon(4)
print(sze.dlugos_boku)
print(sze.calculate_perimeter())
print(sze)