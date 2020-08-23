class Person:
    def __init__(self, navn):
        self._navn = navn

    def hentNavn(self):
        return self._navn
