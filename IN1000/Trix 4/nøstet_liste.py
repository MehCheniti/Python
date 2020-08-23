oliste = []
for i in range(5):
    oliste.append("o")

stjerneliste = []
for i in range(5):
    stjerneliste.append("*")

rutenett = []
rutenett.append(oliste)

rutenett.append(stjerneliste)
rutenett.append(oliste)

for i in rutenett:
    print(i)
