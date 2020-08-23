# Dette programmet ber brukeren om å taste inn et tall og skriver deretter ut
# alle tallene, summen av alle tallene, det største og minste tallet. Brukeren
# kan avslutte programmet ved å taste inn 0.

#Her bruker jeg != for å skille ut 0 fra andre tall. Deretter utvider jeg
#programmet med .append() for å få tallene til å bli lagret i en liste.
liste = []
innlest = input("Vennligst tast inn et tall (tast inn 0 for å avslutte): ")
tall = int(innlest)
while tall != 0:
    liste.append(tall)
    innlest = input("En gang til (tast inn 0 for å avslutte): ")
    tall = int(innlest)
else:
    print("Ha det bra!")

#Her bruker jeg for og in for å printe ut alle elementene i lista.
for element in liste:
    print(liste)

#Her bruker jeg sum funksjonen for å regne ut summen av alle elementene i lista.
minSum = 0
for element in liste:
    print(minSum + sum(liste))

#Her bruker jeg min() og max() for å finne det minste og største elementet i
#lista.
for element in liste:
    print((min(liste)))
for element in liste:
    print((max(liste)))
