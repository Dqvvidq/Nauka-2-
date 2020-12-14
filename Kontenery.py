#metody

print("Witaj")
print("Witaj".upper())

print("Witaj".replace("j","m"))

fruit = list()
print(fruit)

fruit = ["Mango", "Banana", "Aple"]
print(fruit)

fruit.append("Pomelo")
fruit.append("Gruszka")
print(fruit)

fruit.append(True)
fruit.append(20)
fruit.append(20.2)
print(fruit)

print(fruit[0])
print(fruit[3])

fruit[2] = 30
fruit[1] = "Jablko"

print(fruit)

fruit1 = ["jablko", "banan"]
fruit2 = ["arbuz", "pomarancz"]

a = fruit1 + fruit2
print(a)

if "jablko" in a:
    print("jest")
else:
    print("nie ma")

if "pomelo" not in a:
    print("Nie ma")
else:
    print("jest")

print(len(a))
print(len(fruit))

colors = ["czarny", "niebieski", "zielony", "bialy"]
print("Jaki kolor wybrałem?? \nZgadnij!!")
zgadnij = input("Wpisz: ")

if zgadnij in colors:
    print("Zgadłeś!! To jest {}".format(zgadnij))
else:
    print("Nie zgadles!")

#krotki, tuple

my_tuple = ()
print(my_tuple)

rndm = ("M. Jackson", 1958, True)
print(rndm)

print(rndm[1])
print(1958 in rndm)
print(False not in rndm)

#słowniki

owoce = {"agrest": "zielony",
         "porzeczka": "czerwony"}

print(owoce)

owoce["banan"] = "zolty"
owoce["jablko"] = "zielone"
print(owoce)

print("agrest" in owoce)
print("banan" not in owoce)

del owoce["jablko"]

print(owoce)

marka = {"Audi": "A6",
         "Bmw": "e46",
         "Toyota": "camry"}

print("Wpisz Bmw, Audi, Toyota")

n = input("podaj marke:")

if n in marka:
    marka = marka[n]
    print(marka)
else:
    print("Nie znaleziono")


lists = []

rap = ["Kanye West", "Jay Z", "Eminem"]

rock = ["Bob Dylan", "The Beatles"]

djs = ["Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rap)
lists.append(djs)

print(lists)

print(lists[2])


lokacje = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

lokacje.append(la)
lokacje.append(chicago)
print(lokacje)

