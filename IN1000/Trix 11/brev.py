class Brev:
    def __init__(self, avsender, mottaker):
        self._avsender = avsender
        self._mottaker = mottaker
        self._liste = []

    def skrivLinje(self, tekst):
        self._liste.append(tekst)

    def lesBrev(self):
        print("Hei, ", self._mottaker, ".", sep = "")
        print(self._liste[0])
        if len(self._liste) > 0:
            print(self._liste[1])
        print("Hilsen ", self._avsender, ".", sep = "")

brev = Brev("Mehdi", "Cheniti")
brev.skrivLinje("Hva skjer?")
brev.skrivLinje("Bro!")
brev.lesBrev()
