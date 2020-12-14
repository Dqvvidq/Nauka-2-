#Wyzwania kontenery

ulub = ["Peja", "Tede", "Hemp gru"]

print(ulub)

m_geo = []

wro = (32.222, 32.222)
war = (43.333, 32.555)

m_geo.append(wro)
m_geo.append(war)

print(m_geo)

ja = {"Wzrost": 179,
      "Waga": 76,
      "Ulubiony kolor": "Czerwony"}

print(ja)
print("Mozesz mnie zapytac o Wzrost, Wage, Ulubiony kolor")
pytanie = input("Zapytaj mnie: ")

if pytanie in ja:
    ja = ja[pytanie]
    print(ja)
else:
    print("Nie ma")


moi_muzycy = {"Peja": ["Glucha noc", "Szacunek ludzi ulicy"],
              "Tuzza": ["Berlinetta", "Mlody Dorian"]}
print(moi_muzycy)


