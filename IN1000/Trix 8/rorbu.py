from gjest import Gjest

class Rorbu:
    def __init__(self):
        self._gjester = []

    def nyGjest(self, gjestObjekt):
        self._gjester.append(gjestObjekt)
        for gjester in self._gjester:
            gjester.underhold(1)

    def fortellVits(self, heltall):
        for gjester in self._gjester:
            gjester.underhold(heltall)

    def hvorMorsomtHarViDet(self):
        for gjester in self._gjester:
            if gjester.hentUnderholdsningsverdi() / len(self._gjester) < 200:
                return "Kjedelig kveld."
            elif 200 < gjester.hentUnderholdsningsverdi() / len(self._gjester) < 400:
                return "Dette var jo litt gøy."
            elif 400 < gjester.hentUnderholdsningsverdi() / len(self._gjester) < 600:
                return "Dette var artig!"
            elif gjester.hentUnderholdsningsverdi() / len(self._gjester) > 600:
                return "Dra på Lopphavet - bi dæ godtar no så gyt e!"

    def hentAntallGjester(self):
        return len(self._gjester)
