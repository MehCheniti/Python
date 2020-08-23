liste = ["Hei", "Python!"]

teller = 0
while teller < len(liste):
    print(teller)
    teller += 1

innlest = input("Hva? ")
liste.append(innlest)
print(liste)
