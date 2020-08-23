class Student:
    def __init__(self, navn, brukernavn, telefonnummer):
        self._navn = navn
        self._brukernavn = brukernavn
        self._telefonnummer = telefonnummer

    def printInfo(self):
        print("Navn: ", self._navn, ".", sep = "")
        print("Bukernavn: ", self._brukernavn, ".", sep = "")
        print("Telefonnummer: ", self._telefonnummer, ".", sep = "")
