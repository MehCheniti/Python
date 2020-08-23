class Rektangel:
    def __init__(self, lengde, bredde):
        self._lengde = lengde
        self._bredde = bredde

    def ok_lengde(self, okning):
        self._lengde += okning

    def ok_bredde(self, okning):
        self._bredde += okning

    def areal(self):
        print(self._lengde * self._bredde)

    def omkrets(self):
        print((self._lengde)*2 + (self._bredde)*2)

    def red_lengde(self, ned):
        self._lengde -= ned

    def red_bredde(self, ned):
        self._bredde -= ned


rektangel1 = Rektangel(17, 34)
rektangel2 = Rektangel(18, 35)

rektangel1.areal()
rektangel2.areal()

rektangel1.ok_lengde(10)
rektangel2.ok_bredde(20)

rektangel1.omkrets()
rektangel2.omkrets()
