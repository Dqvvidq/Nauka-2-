#Operacje na łańcuchach znaków

author = "kawka"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

print(author[-1])
print(author[-2])
print(author[-3])

ff = "FC. Barcelona"
print(ff)
ff = "Real. Madrit"
print(ff)

a = "kot "
b = "w"
c = " butach"

print(a + b + c)
print("kot" + " w" + " butach")

print(a * 3)
print("kot " * 3)

print("Nie pytaj komu bije dzwon".upper())
print(a.upper())

print("W".lower())

print(b.capitalize())
print("kot".capitalize())

print("Wiliam {}".format("Szekspir"))

print("Kot i {}".format(a))

n1 = input("Wpisz w co lubisz grac: ")
n2 = input("I jak bardzo: ")

print("Lubie grac w {} bardzo {}".format(n1, n2))

print("Hej. Siema".split("."))

first_tree = "abc"
rezultat = "+".join(first_tree)
print(rezultat)

panstwa = ["Polska", "Austria", "Niemcy"]
pp = " ".join(panstwa)
print(pp)

s = "    to     "
s = s.split()
print(s)

equ = "Ostry wicher mrozi"
equ = equ.replace("r", "q")
print(equ)

print("imperialny".index("r"))

print("kot" in "kot w butach")
print("kat" in "kot w butach")

print("odpowiedziała mu: \"Owszem.\"")

print("wiersz1\nwiersz2\nwiersz3\n")

ficts = ["Cavel", "Camus", "Owrell", "Huxley", "Austin"]
print(ficts[0:3])

ivan = "A życ tak na skraju zguby trzeba samotnie"
print(ivan[0:10])
print(ivan[26:41])
print(ivan[:10])
print(ivan[26:])
print(ivan[:])


