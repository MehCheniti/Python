from person import Person

class Bil:
    def __init__(self, farge, merke):
        self._farge = farge
        self._merke = merke

    def bilLaan(self):
        return Bil(self._farge, self._merke)
