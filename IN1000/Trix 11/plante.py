class Plante:
    def __init__(self, vannbeholder, maksgrenseVann):
        self._vannbeholder = vannbeholder
        self._maksgrenseVann = maksgrenseVann

    def vannPlante(self, vannCl):
        self._vannbeholder += vannCl
        if self._vannbeholder > self._maksgrenseVann:
            return False

    def nyDag(self):
        self._vannbeholder -= 20
        if self._vannbeholder < 0:
            return False

    def levende(self):
        if self._vannbeholder > self._maksgrenseVann:
            return "Planten er død."
        elif self._vannbeholder < 0:
            return "Planten er død."
        else:
            return "Planten er levende."

plante1 = Plante(40, 40)
plante2 = Plante(90, 90)

plante1.vannPlante(10)
plante2.vannPlante(10)

plante1.nyDag()
plante1.nyDag()
plante2.nyDag()
plante2.nyDag()

print(plante1.levende())
print(plante2.levende())
