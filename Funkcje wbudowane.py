#Funkcje wbudowane

print(len("Monty"))

print(len("Python"))

print(type(str(100)))

print(str(100))

print(int("1"))

print(float(100))





while False:
    age = input("Wpisz wiek: ")
    int_age = int(age)
    if int_age >= 25:
        print("Jesteś stary")
    elif int_age >= 18:
        print("Jesteś dorosły")
    else:
        print("Jesteś młody")


def even_odd(m):
    if m % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba nie jest parzysta")

even_odd(6)


n = input("Wpisz liczbę: ")
n = int(n)

if n % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nie parzysta")


def p(x=2):
    return x * x

wynik = p()
print(wynik)
wynik1 = p(4)
print(wynik1)
