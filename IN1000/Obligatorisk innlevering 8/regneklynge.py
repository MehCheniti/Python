from node import Node
from rack import Rack

class Regneklynge:

    """ Denne klassen representerer regneklynger som inneholder racks med
    noder. """

	# Oppretter en liste regneklynge med max noder per rack som parameter.
    def __init__(self, noderPerRack):
        self._regneklynge = []
        self._noderPerRack = noderPerRack

	## Alternativ konstruktor for de som loser oppgave d). Kan ellers ignoreres
	## Leser data om regneklynge fra fil, bygger datastrukturen.
	# @param filnavn filene der dataene for regneklyngen ligger
#    def __init__(self, filnavn):
#        pass

	# Plasserer en node inn i et rack med ledig plass, eller i et nytt rack.
    def settInnNode(self, node):
        nyttRack = Rack()

        # Lager et nytt rack om det ikke er noen racks i regneklyngen.
        if self.antRacks() == 0:
            self._regneklynge.append(nyttRack)

        # lastRack blir lik det siste rack objektet i self._regneklynge.
        lastRack = self._regneklynge[-1]

        # Sjekker først om nodene i lastRack er lik maksimum noder per rack.
        # Hvis ja, legger jeg til et rack-objekt i regneklynge og setter inn et
        # node-objekt.
        if lastRack.getAntNoder() == self._noderPerRack:
            self._regneklynge.append(nyttRack)
            nyttRack.settInn(node)

        # Deretter sjekker jeg om nodene i lastRack er færre enn maksimum noder
        # per rack.
        # Hvis ja, legger jeg til et node-objekt i lastRack.
        elif lastRack.getAntNoder() < self._noderPerRack:
            lastRack.settInn(node)

        # Til slutt, sjekker jeg om nodene i lastRack er flere enn maksimum
        # noder per rack.
        # Hvis ja, legger jeg til et rack-objekt i regneklynge og setter inn et
        # node-objekt i lastRack.
        elif lastRack.getAntNoder() > self._noderPerRack:
            self._regneklynge.append(nyttRack)
            lastRack.settInn(node)

	# Returnerer totalt antall prosessorer i hele regneklyngen.
    def antProsessorer(self):
        antallProcessorer = 0

        # Itirerer gjennom regneklyngen for å finne antall processorer i hele
        # regneklyngen.
        for racks in self._regneklynge:
            antallProcessorer += racks.antProsessorer()
        return antallProcessorer

	# Returnerer antall noder i regneklyngen med minne over angitt grense.
    def noderMedNokMinne(self, paakrevdMinne):
        noderMedNokMinne = 0

        # Itirerer gjennom regneklyngen for å finne antall noder med minne over
        # gitt grense.
        for racks in self._regneklynge:
            noderMedNokMinne += racks.noderMedNokMinne(paakrevdMinne)
        return noderMedNokMinne

	# Returnerer antall racks i regneklyngen.
    def antRacks(self):
        return len(self._regneklynge)
