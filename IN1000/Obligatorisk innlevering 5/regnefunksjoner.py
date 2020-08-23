# Dette programmet skriver ut resultatet av 17 + 34 og konverterer 7 tommer til
# cm. Etter det spør det om 2 tall og skriver ut summering, subtraksjon og
# divisjon av de 2 tallene. Til slutt spør det om et siste tall og konverterer
# det tallet fra tommer til cm.

#Her velger jeg 17 og 34 som testargumenter.
def addisjon(tall1, tall2):
    return tall1 + tall2

print("17 + 34 = ", addisjon(17, 34), ".", sep="")

#Her bruker jeg assert for å sjekke resultatene.
def subtraksjon(tall3, tall4):
    return tall3 - tall4

def divisjon(tall5, tall6):
    return tall5 / tall6

assert subtraksjon(17, 34) == -17
assert subtraksjon(-17, -34) == 17
assert subtraksjon(17, -34) == 51

assert divisjon(17, 34) == 0.5
assert divisjon(-17, -34) == 0.5
assert divisjon(17, -34) == -0.5

#Her velger jeg 7 tommer som eksempel.
def tommerTilCm(antallTommer):
    assert antallTommer > 0
    return antallTommer * 2.54

print("7 tommer er lik ", tommerTilCm(7), " cm.", sep="")

#
def skrivBeregninger():
    tall7 = float(input("Vennligst skriv inn et tall: "))
    tall8 = float(input("Vennligst skriv inn et annet tall: "))
    print(tall7, " + ", tall8, " = ", addisjon(tall7, tall8), ".", sep="")
    print(tall7, " - ", tall8, " = ", subtraksjon(tall7, tall8), ".", sep="")
    print(tall7, " / ", tall8, " = ", divisjon(tall7, tall8), ".", sep="")

    tall9 = float(input("Vennligst skriv inn et siste tall (i tommer): "))
    print(tall9, " tommer er lik ", tommerTilCm(tall9), " cm.", sep="")

skrivBeregninger()
