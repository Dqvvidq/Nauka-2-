name = "Ted"
for litera in name:
    print(litera)

shows = ["Jaka to melodia", "Spadkobiercy", "Familiada"]
for show in shows:
    print(show)

coms = ("Programowanie", "Znajomi", "Hillout")
for com in coms:
    print(com)

people = {"Flower": "Wzorce projektowe",
          "Knuth": "Algorytmy",
          "Stroustrup": "C++"}

for pep in people:
    print(pep)

tv = ["Jaka to melodia", "Spadkobiercy", "Familiada"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)

all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)

for i in range(1, 11):
    print(i)

x = 10
while x > 10:
    print("{}".format(x))
    x -= 1
print("Szczęśliwego nowego roku!")

for i in range(0, 100):
    print(i)
    if i == 2:
        break

qs = ["Jak masz na imię?", "Jaki jest twoj ulubiony kolor?", "Jakie masz zadanie?"]
n = 0
while True:
    print("Wpisz q zeby zakonczyc")
    a = input(qs[n])
    if a == "q":
        print("Koniec")
        break
    n = (n + 1) % 3

for i in range(1, 5):
    if i == 3:
        continue
    print(i)

i = 0
while i <= 5:
    if i == 3:
        i += 1
    print(i)
    i += 1

for i in range(1, 4):
    print(i)
    for leter in ["a", "b", "c"]:
        print(leter)

list1 = [1, 2, 3]
list2 = [3, 4, 5]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

while input("t czy n?") != "n":
    for i in range(1, 6):
        print(i)


