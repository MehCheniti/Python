# Dette programmet ber brukeren om å taste inn fire navn og sjekker deretter om
# brukeren har tastet inn navnet mitt eller ikke.

#Her bruker jeg .append() for å legge inn et nytt tall på lista.
liste = [1, 2, 3]
liste.append(4)
print(liste[0], liste[2])

#Her bruker jeg en prosedyre for å unngå å skrive så mange linjer.
nyListe = []
def navn():
    nyListe.append(str(input("Vennligst oppgi et navn: ")))
navn()
navn()
navn()
navn()

#Her bruker jeg if og in for å sjekke om 'Mehdi' eller 'mehdi' finnes i lista.
if "Mehdi" in nyListe or "mehdi" in nyListe:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#Her bruker jeg .remove() for å fjerne de to siste elementene fra lista.
nyereListe = liste + nyListe
print(nyereListe)
nyereListe.remove(nyereListe[7])
nyereListe.remove(nyereListe[6])
print(nyereListe)
