from sokk import Sokk

class Skuff:
    def __init__(self):
        self._mineHøyreSokker = []
        self._mineVenstreSokker = []

    def settInnSokk(self, sokken):
        if sokken.hentSide() == "høyre":
            self._mineHøyreSokker.append(sokken)
        elif sokken.hentSide() == "venstre":
            self._mineVenstreSokker.append(sokken)

    def sjekkStatus(self):
        if len(self._mineHøyreSokker) == len(self._mineVenstreSokker):
            print("Alt i orden.")
        else:
            print("Ulikt antall høyre- og venstresokker.")
