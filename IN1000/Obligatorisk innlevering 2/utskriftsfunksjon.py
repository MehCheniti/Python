# Dette programmet ber brukeren om å skrive inn navn og bosted for å så skrive
# dem ut.

#Her bruker jeg sep="" for å eliminere mellomrommene.
navn = input("Skriv inn navn: ")
bosted = input("Hvor kommer du fra? ")
print("Hei, ", navn, "! ", "Du er fra ", bosted, ".", sep="")

#Her bruker jeg def() for å lage en prosedyre.
def hilsen ():
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra? ")
    print("Hei, ", navn, "! ", "Du er fra ", bosted, ".", sep="")
hilsen()
hilsen()
hilsen()
