#Zasięg



#def f():
    #print(x)
    #print(y)
    #print(z)



def g():
    p = 2
    print(p)

#przechwytywane wyjatkow

g()
print("Podziel dwie liczby")
a = input("Wpisz pierwsza liczbe: ")
b = input("Wpisz druga liczbe: ")
a = int(a)
b = int(b)
try:
    print(a/b)
except (ZeroDivisionError, ValueError):
    print("Nieprawidłowe dane")

#lancuchy dokumentujace

def add(x, y):
    """
    zwraca x + y
    :param x: int
    :param y: int
    :return: x + y
    """
    return x + y

print(add(1, 3))

def p(x):
    """
    x do kwadratu
    :param x: int
    :return: x ** 2
    """
    return x ** 2

print(p(3))

p = "lancuch znakow"
def lancuch(p):
    print(p)

lancuch(p)

def trzy(x, y, z):
    """
    dodaje wszystko
    :param x: int
    :param y: int
    :param z: int
    :return: x + z + y
    """
    return x + y + z

print(trzy(1, 2, 3))



def pierw(x):
    return x / 2

def dru(d):
    return d * 4


d = pierw(4)
print(dru(d))




def str(x):
    """
    pobiera x i wzwraca jako float
    :param x: int/float
    :return: float
    """
    try:
        print(float(x))
    except ValueError:
        print("Wpisz liczbe!! A nie łancuch znakow")

str("czesc")
str(2)

