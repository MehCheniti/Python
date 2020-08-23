# Oppgave 5: Person klasse
# Filnavn: personKlasse.py
# 1. Lag en klasse Person med hoyde og vekt som instansvariabler.
# 2. Lag en metode som skriver ut høyden og vekten.
# 3. Test klassen din.

class Person:
    def __init__(self, hoyde, vekt):
        self._hoyde = hoyde
        self._vekt = vekt

    def skrivUt(self):
        print("Høyde: ", self._hoyde, " CM.", sep="")
        print("Vekt: ", self._vekt, " KG.", sep="")

person = Person(198, 90)

person.skrivUt()
