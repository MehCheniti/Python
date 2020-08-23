class Hund:
    def __init__(self, alder, vekt, metthet = 10):
        self._alder = alder
        self._vekt = vekt
        self._metthet = metthet

    def hentUtAlder(self):
        return self._alder

    def hentUtVekt(self):
        return self._vekt

    def spring(self):
        self._metthet -= 1
        if self._metthet < 5:
            self._vekt -= 1

    def spis(self):
        innlest = int(input("Hvor mange kjøttboller har hunden spist? "))
        self._metthet += innlest #Her øker jeg metthet med input-verdien.
        if self._metthet > 7:
            self._vekt +=  1
