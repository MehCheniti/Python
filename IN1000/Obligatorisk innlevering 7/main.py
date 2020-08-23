from spillebrett import Spillebrett

def main():
    # Her ber jeg brukeren om å oppgi antall rader og kolonner.
    rader = int(input("Vennligst oppgi antall rader: "))
    kolonner = int(input("Vennligst oppgi antall kolonner: "))

    spill = Spillebrett(rader, kolonner)
    print("\n")
    spill.tegnBrett()
    print("\n")
    print("Antall levende celler: ", spill.finnAntallLevende(), ".", sep = "")
    print("\n")

    inp = str(input(
    "Vil du fortsette? Trykk enter for å fortsette eller tast inn q for å avslutte: "
    ))
    # Her bruker jeg en while-løkke for å få programmet til å kjøre så lenge
    # brukeren vil.
    while inp != "q":
        spill.oppdatering()
        print("\n")
        spill.tegnBrett()
        print("\n")
        print("Antall levende celler: ", spill.finnAntallLevende(), ".",
        sep = "")
        print("Generasjonsnummer: ", spill.generasjonsnummer(), ".", sep = "")
        print("\n")
        inp = str(input(
        "Vil du fortsette? Trykk enter for å fortsette eller tast inn q for å avslutte: "
        ))

main()
