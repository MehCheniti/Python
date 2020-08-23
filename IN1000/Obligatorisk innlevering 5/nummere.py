# Oppgave 5: Nummere
# Filnavn: nummere.py
# 1. Åpn en tekstfil (nummere.txt) som inneholder tallene fra 1 til 10.
# 2. Lag en tom liste minListe.
# 3. Skriv en funksjon minFunksjon som tar imot en liste som parameter.
# 4. Funksjonen skal da legge til alle tallene fra tekstfilen i listen, og
# deretter returnere lengden av listen.
# 5. Kall minFunksjon med minListe som argument og skriv ut resultatet.

# Dette programmet skriver ut lengden av en liste.

fil = open("nummere.txt", "r")

minListe = []

def minFunksjon(liste):
    for nummere in fil:
        liste.append(nummere)
    return len(liste)

print("Lengden av listen er ", minFunksjon(minListe), ".", sep="")
