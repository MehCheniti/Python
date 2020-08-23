from random import randint
from celle import Celle

class Spillebrett:

    """Dette er en klasse som beskriver et todimensjonalt brett som
    inneholder celler. Den skal også oppdatere celler som skal endre status."""

    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []

        # Her lager jeg en nøstet for-løkke for å fylle self._rutenett med
        # Celle-objekter.
        for i in range(self._rader):
            rad = []
            for j in range(self._kolonner):
                rad.append(Celle())
            self._rutenett.append(rad)

        self._generasjonsnummer = 0
        self.generer()

    def tegnBrett(self):
        # Her lager jeg en nøstet for-løkke for å kunne skrive ut hvert element
        # i self._rutenett.
        for i in self._rutenett:
            for j in i:
                print(j.hentStatusTegn(), end = " | ")
            # Her bruker ganger jeg ---- med antall kolonner for å det til å se
            # fint ut.
            print("\n" + "----"*self._kolonner)

    def oppdatering(self):
        dødTilLevende = []
        levendeTilDød = []

        for i in range(len(self._rutenett)):
            for j in range(len(self._rutenett[i])):
                # Her lager jeg en liste for verdiene finnNabo returnerer.
                naboliste = self.finnNabo(i, j)
                # Her sjekker jeg både om cellen har 2 eller 3 levende naboer
                # og om cellen er levende.
                if (len(naboliste) == 2 or len(naboliste) == 3
                ) and self._rutenett[i][j].erLevende():
                    dødTilLevende.append(self._rutenett[i][j])
                # Her sjekker jeg både om cellen ikke er levende og om den har
                # 3 levende naboer.
                elif not self._rutenett[i][j].erLevende() and len(naboliste
                ) == 3:
                    dødTilLevende.append(self._rutenett[i][j])
                # Her sjekker jeg hvis cellen skal fortsette å være død eller
                # drepes etter oppdateringen.
                else:
                    levendeTilDød.append(self._rutenett[i][j])

        # Her setter jeg objektene som skal leve til "levende".
        for i in dødTilLevende:
            i.settLevende()
        #Her setter jeg objektene som skal dø til "død"
        for i in levendeTilDød:
            i.settDoed()

        self._generasjonsnummer += 1

    def finnAntallLevende(self):
        teller = 0
        # Her bruker jeg en nøstet for-løkke for å finne ut hvor mange celler
        # er levende.
        for i in range(self._rader):
            for j in range(self._kolonner):
                if self._rutenett[i][j].erLevende() == True:
                    teller += 1
        return teller

    def generer(self):
        for i in range(self._rader):
            for j in range(self._kolonner):
                rand = randint(0,3)
                if rand == 3:
                    self._rutenett[i][j].settLevende()

    def finnNabo (self, rad, kolonne):
        naboliste = []
        for i in range (-1, 2):
            for j in range (-1, 2):
                naboRad = rad + i
                naboKolonne = kolonne + j
                if (naboRad == rad and naboKolonne == kolonne) != True:
                    if (naboRad < 0 or naboKolonne < 0 or naboRad >
                    self._rader-1 or naboKolonne > self._kolonner-1) != True:
                        # Her endrer jeg på metoden slik at den returnerer en
                        # liste kun av levende naboer.
                        if self._rutenett[naboRad][naboKolonne].erLevende():
                            naboliste.append(self._rutenett[naboRad]
                            [naboKolonne])
        return naboliste

    # Her definerer jeg en metode som returnerer generasjonsnummeret.
    def generasjonsnummer(self):
        return self._generasjonsnummer
