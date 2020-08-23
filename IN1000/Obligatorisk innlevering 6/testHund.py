from hund import Hund

def hovedprogram():

    hund = Hund(5, 50)

    hund.spring()
    hund.spis()

    print("Vekten er: ", hund.hentUtVekt(), " KG.", sep="")

    hund.spring()
    hund.spis()

    print("Den nye vekten er: ", hund.hentUtVekt(), " KG.", sep="")

hovedprogram()
