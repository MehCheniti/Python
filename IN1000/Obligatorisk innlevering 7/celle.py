class Celle:

    """ Dette er en klasse som beskriver en celles status i spillet. """
# Her skriver jeg status = "død" for å få statusen "død" som utganspunkt.
    def __init__(self, status = "død"):
        self._status = status

    def settDoed(self):
        self._status = "død"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        if self._status == "levende":
            return True
        elif self._status == "død":
            return False
# Her bruker jeg metoden erLevende() inne i metoden hentStatusTegn() for å
# bruke de boolske utrykkene.
    def hentStatusTegn(self):
        if self.erLevende() == True:
            return "O"
        elif self.erLevende() == False:
            return "."
