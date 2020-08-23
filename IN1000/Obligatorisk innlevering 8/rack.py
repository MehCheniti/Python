from node import Node

class Rack:

    """ Denne klassen representerer racks som skal plasseres i en
    regneklynge. """

    def __init__(self):
        self._rack = []

	# Plasserer en ny node i racket.
    def settInn(self, node):
        self._rack.append(node)

	# Returnerer antall noder i racket.
    def getAntNoder(self):
        return len(self._rack)

	# Returnerer antall prosessorer i nodene i racket.
    def antProsessorer(self):
        antalProcessorer = 0

        # Itirerer gjennom racks for å finne antall processorer.
        for noder in self._rack:
            antalProcessorer += noder.antProsessorer()
        return antalProcessorer

	# Returnerer antall noder med minne over gitt grense.
    def noderMedNokMinne(self, paakrevdMinne):
        noderMedNokMinne = 0

        # Itirerer gjennom racks for å finne antall noder med minne over gitt
        # grense.
        for noder in self._rack:
            if noder.nokMinne(paakrevdMinne):
                noderMedNokMinne += 1
        return noderMedNokMinne
