c = "Camus"

print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

p1 = input("Co wczoraj napisałes?: ")
p2 = input("Do kogo to wyslales?: ")
print("Wczoraj napisałem {} i wysłałem do {}".format(p1, p2))

zd = "adous Haxley urodził sie w 1894 roku"
zd = zd.capitalize()
print(zd)

lista = ["Zwinny", "lis", "przeskoczył", "nad", "leniwym", "psem", "."]
b = " ".join(lista)
print(b)

zd = "W czasie suszy szosa sucha."
zd = zd.replace("s", "$")
print(zd)

print("Hemingway".index("m"))

got = "Dama"
print(got)

print("trzy " * 3)

dl = "Dlugo na szturm i szaniec poglądał w milczeniu. Na koniec rzekł: 'Stracona'."
dl = dl.split(".")
print(dl[1])
