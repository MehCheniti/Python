class Motorsykkel:
    def __init__(self, merke, registreringsnummer, kilometerstand):
        self._merke = merke
        self._registreringsnummer = registreringsnummer
        self._kilometerstand = kilometerstand

    def kjor(self, km):
        self._kilometerstand += km #Her øker jeg kilometerstand med km.

    def hentKilometerstand(self):
        return self._kilometerstand

    def skrivUt(self):
        print("Merken er ", self._merke, ".", sep="")
        print("Registreringsnummer: ", self._registreringsnummer, ".", sep="")
        print("Total kilometerstand: ", self._kilometerstand, ".", sep="")
