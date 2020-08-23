navn = open("navn.txt", "r")

liste = []

for i in navn:
    liste.append(i.rstrip())

print(liste)
