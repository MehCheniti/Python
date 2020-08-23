class Person:
    def __init__(self, navn, ektefelle, status = "ugift"):
        self._navn = navn
        self._ektefelle = ektefelle
        self._status = status

    def settGift(self):
        self._status = "gift"

    def minStatus(self):
        if self._status == "gift":
            print(self._ektefelle)
        else:
            print("Du er singel.")

    def bryllup(self, ektefelleNavn):
        ektefelleNavn = self._ektefelle
