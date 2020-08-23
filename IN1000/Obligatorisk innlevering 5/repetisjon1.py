# Dette programmet ber brukeren om å taste inn tekststrenger og skriver da ut
# en sammenslått versjon av tekstrengene.

mineOrd = []

def slaaSammen(streng1, streng2):
    return str(streng1) + str(streng2)

def skrivUt(liste):
    for i in liste:
        print("De sammenslåtte tekststrengene er ", i, ".", sep="")

#Her kan brukeren avslutte programmet ved å taste inn noe som != y.
inp = str(input("Tast inn y for å begynne/ fortsette: "))

while inp == "y":
    inp2 = str(input("Tast inn enten i, u eller s: "))
    #Her bruker jeg .append() for å legge til tekstrengene inne i mineOrd
    #listen.
    if inp2 == "i":
        inp3 = str(input("Tast inn en tekststreng: "))
        inp4 = str(input("Tast inn en annen tekststreng: "))
        mineOrd.append(slaaSammen(inp3, inp4))

    elif inp2 == "u":
        skrivUt(mineOrd)
    #Her bruker jeg break for å avslutte programmet når brukeren taster inn "s".
    elif inp2 == "s":
        break

    inp = str(input("Tast inn y for å begynne/ fortsette: "))
