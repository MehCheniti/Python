from sokk import Sokk
from skuff import Skuff

def hovedprogram():
    sokk1 = Sokk("høyre")
    sokk2 = Sokk("venstre")
    skuff1 = Skuff()

    skuff1.settInnSokk(sokk1)
    skuff1.settInnSokk(sokk2)

    skuff1.sjekkStatus()

    sokk3 = Sokk("venstre")
    skuff1.settInnSokk(sokk3)

    skuff1.sjekkStatus()

hovedprogram()
