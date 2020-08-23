beholdning = {}

begFor = str(input("Vil du begynne? (tast y for å avslutte) "))
while begFor != "y":
    grønnsak = str(input("Grønnsak? "))
    pris = int(input("Pris? "))
    beholdning[grønnsak] = pris
    begFor = str(input("Vil du fortsette? (tast y for å avslutte) "))

for i, e in beholdning.items():
    print(i, " : ", e)
