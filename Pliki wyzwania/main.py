import csv

pyt = input("Ile maz lat?:  ")

st = open("st.txt", "w")
st.write("On ma {} lat".format(pyt))
st.close()

with open("st.txt", "r") as f:
    print(f.read())

lista = [["Top Gun", "Oceans Eleven", "Raport mniejszosci"], ["Titanic", "Ostatni Jedi", "Incepcja"],
         ["Pulp Fiction", "Człowiek w ogniu", "Seksmisja"]]

with open("film.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(lista[0])
    write.writerow(lista[1])
    write.writerow(lista[2])