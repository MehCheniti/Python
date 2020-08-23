class Bil:
    def __init__(self, eier, merke):
        self._eier = eier
        self._merke = merke

    def eierOgMerke(self):
        print("Eieren er ", self._eier, ".", sep="")
        print("Merken er ", self._merke, ".", sep="")

Bil("Mehdi", "Maclaren").eierOgMerke()
Bil("Mostafa", "Peugeot 108").eierOgMerke()
