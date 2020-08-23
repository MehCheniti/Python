class Gjest:
    def __init__(self):
        self._underholdningsverdi = 0

    def underhold(self, heltallsverdi):
        self._underholdningsverdi += heltallsverdi

    def hentUnderholdsningsverdi(self):
        return self._underholdningsverdi
