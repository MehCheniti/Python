class EspressoMaskin:
    def __innit__(self, vann = 1000):
        self._vann = vann

    # Lag espresso dersom det er nok vann
    def lag_espresso(self):
        if self._vann >= 40:
            print("Her har du en espresso!")
        else:
            print("Ikke nok vann.")

    # Lag lungo dersom det er nok vann
    def lag_lungo(self):
        if self._vann >= 110:
            print("Her har du en lugo!")
        else:
            print("Ikke nok vann.")

    # Fyll paa et gitt antall milliliter vann, dersom det er plass
    def fyll_vall(self, ml):
        if self._vann < 1000:
            self._vann += ml
        elif self._vann >= 1000:
            print("Ikke nok plass.")

    # Les av maalestrekene på vanntanken og tilgjengelig vann i ml
    def hent_vannmengde(self):
        print(self._vann, " ml.", sep="")
