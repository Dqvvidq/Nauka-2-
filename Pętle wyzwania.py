filmy = ["Noc zywych trupow", "Ekipa", "Rodzina Soprano", "Pamietniki wampirow"]

for i in filmy:
    print(i)

for i in range(25, 51):
    print(i)

for i, film in enumerate(filmy):
    print(i)
    print(film)

lista1 = [8, 19, 148, 4]
lista2 = [9, 1, 33, 83]

wsio =[]

for i in lista1:
    for j in lista2:
        x = i * j
        wsio.append(x)

print(wsio)