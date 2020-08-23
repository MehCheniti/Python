# Oppgave 5: Favoritt navn
# Filnavn: favoritt.py
# 1. Lag en tom liste med navnet favoritt.
# 2. Lag en while-løkke som leser inn navn fra brukeren helt til brukeren
# taster inn "quit". Deretter skal du endre løkken slik at den lagrer navnene
# brukeren taster inn i listen favoritt.
# 3. Print ut listen favoritt.
# 4. Nå skal du be brukeren om å velge yndlingsnavnet ut av navnene på listen.
# Programmet skal da skrive ut det navnet.

# Dette programmet ber brukeren om å skrive inn navn og printer deretter ut
# navnet som brukeren foretrekker mest.

favoritt = []

innlest = input("Vennligst tast inn et navn (tast inn quit for å avslutte): ")
navn = str(innlest)
while navn != "quit":
    favoritt.append(navn)
    innlest = input("Tast inn et annet navn (tast inn quit for å avslutte): ")
    navn = str(innlest)

print(favoritt)

innlest2 = int(input(
"Hvilket navn foretrekker du? (PS: tast inn 0 for det forste navnet, 1 for det andre, osv...) "
))
favorittNavn = favoritt[innlest2]
print("Yndlingsnavnet ditt er ", favorittNavn, ".", sep="")
