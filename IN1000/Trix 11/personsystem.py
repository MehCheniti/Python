from person2 import Person

class Personsystem:
    def __init__(self):
        self._listeAvPersoner = []

    def leggTilPerson(self, personObjekt):
        self._listeAvPersoner.append(personObjekt)

    def finnPerson(self, navn):
        for personer in self._listeAvPersoner:
            if navn == personer.hentNavn():
                return personer
            return None
