# Dette programmet ber brukeren om å legge til to varenavn med prisene deres,
# for å så printe ut en liste av forskjellige varer og priser.

#Her bruker jeg {} for å lage en ordbok.
ordbok = {"melk" : 14.90, "brod" : 24.90, "yoghurt" : 12.90, "pizza" : 39.90}
print(ordbok)

#Her bruker jeg [] for å legge til to objekter i ordboken.
vare1 = input("Tast inn en vare: ")
pris1 = float(input("Tast inn prisen: "))
vare2 = input("Tast inn en annen vare: ")
pris2 = float(input("Tast inn prisen: "))
ordbok[vare1] = pris1
ordbok[vare2] = pris2
print(ordbok)
