personer = {}

f = input("Fortsette? (tast inn y for å fortsette) ")
while f == "y":
    navn = str(input("Navn? "))
    alder = int(input("Alder? "))
    personer[navn] = alder
    f = input("Fortsette? (tast inn y for å fortsette) ")

bokstav = str(input("Bokstav? "))
while len(bokstav) != 1:
    bokstav = str(input("Bokstav? "))

bokstav = bokstav.lower()
for i in personer:
    if i[0].lower() == bokstav:
        print(i, personer[i])
