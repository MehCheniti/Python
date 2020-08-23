class Node:

    """ Denne klassen representerer noder som skal plasseres i racks. """

    def __init__(self, minne, antPros):
        self._minne = minne
        self._antPros = antPros

    # Returnerer antall prosessorer.
    def antProsessorer(self):
        return self._antPros

    # Returnerer True hvis noden har nok minne for et program.
    def nokMinne(self, paakrevdMinne):
        if self._minne >= paakrevdMinne:
            return True
