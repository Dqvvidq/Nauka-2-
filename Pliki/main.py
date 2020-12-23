import os
import csv

st = open("st.txt", "w")
st.write("Czesc.. zapisano z pythona!")
st.close()

with open("sts.txt", "w") as f:
    f.write("Czesc... zapisano tez z pythona")

with open("st.txt", "r") as f:
    print(f.read())

my_list = []

print(my_list)

with open("sts.txt", "r") as f:
    my_list.append(f.read())

print(my_list)

with open("css.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["jeden", "dwa", "trzy"])
    write.writerow(["cztery", "piec", "szesc"])

with open("css.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
