#Instrukcje warunkowe

home = "Ameryka"
if home == "Ameryka":
    print("Witaj Ameryko!")
else:
    print("Witaj swiecie!")

while True:
    print("Wpisz 0 aby zakonczyc")
    x = input("Wpisz liczbę: ")
    x = int(x)
    if x == 2:
        print("Liczba wynosi 2")
    if x % 2 == 0:
        print("Liczba jest parzysta")
    if x % 2 != 0:
        print("Liczba jest nie przysta")
    if x == 0:
        print("Koniec programu")
        break

x = 10
y = 11
if x == 10:
    if y == 11:
        print(x + y)

home = "Tajlandia"
if home == "Japonia":
    print("Witaj Japonio")
elif home == "Dania":
    print("Witaj Danio")
elif home == "Francja":
    print("Witaj Francjo")
elif home == "Tajlandia":
    print("Witaj Tajlandio")
else:
    print("Nie ma")

x = 100
if x == 10:
    print("10!")
elif x == 20:
    print("20!")
elif x == 30:
    print("30!")
else:
    print("Nie wiem")

if x == 100:
    print("X jest rowne 100!!")

if x % 2 == 0:
    print("X jest parzyste")
else:
    print("X nie jest parzyste")