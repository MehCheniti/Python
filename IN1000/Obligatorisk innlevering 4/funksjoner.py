# Dette programmet ber brukeren om å taste inn en setning og en bokstav og
# skriver deretter ut hvor mange ganger bokstaven forekommer i setningen.

#Her valgte jeg 1, 2 og 3, 4 som argumenter.
def adder(tall1, tall2):
    print("Summen er ", tall1 + tall2, ".", sep="")
adder(1, 2)
adder(3, 4)

#Her bruker jeg .count() for å regne hvor mange ganger en bokstav forekommer i
#en setning. (Oppgave 3): etter det endret jeg koden slik at den benytter en
#funksjon som heter tellForekomst2.
def tellForekomst2(tekststreng, bokstav):
    bokstaviTekststreng = tekststreng.count(bokstav)
    print("Bokstaven ", bokstav, " forekommer ", bokstaviTekststreng,
    " gang(er) i setningen ", tekststreng, ".", sep="")
tellForekomst2(str(input("Vennligst tast inn en setning: ")),
str(input("Vennligst tast inn en bokstav: ")))

#def tellForekomst(minTekst, minBokstav):
#    minBokstaviTekst = minTekst.count(minBokstav)
#    return(minBokstaviTekst)
#tellForekomst()
