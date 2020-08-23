# encoding: utf-8

                    ### 1 Lingvistiske nivåer ###
# I lingvistikk opererer man i 6 nivåer.
# Første nivå er fonetikk, som har fokus på lyder.
# Andre nivå er fonologi, som har med både lyder og språk å gjøre.
# Tredje er morfologi, som handler om morfemer og ord.
# Fjerde er syntaks, som er læren til hvordan ord settes sammen til setninger.
# Femte er semantikk, som dreier seg om innholdet til setninger, det vil si
# deres meninger og betydninger.
# Og til slutt har vi siste nivå som er pragmatikk.
# Den handler om hvordan kontekst kan bidra til meninger og betydninger til
# fraser.

                    ### 2 Morfologi ###
# Bundne morfemer har som regel at de ikke kan funke som ord alene, det vil si
# at de har en grammatisk oppgave (de kan være en verb, substantiv osv. …) mens
# frie morfemer kan fungere som et ord alene. Eksempler til bundne morfemer er
# «spiser», «mannen» og til frie morfemer: «bil», «kjørefil».
# De bundne morfemene kan deles i undergrupper som heter bøyningsmorfemer og
# avledningsmorfemer. Bøyningsmorfemer endrer ordets bøyning uten å endre
# ordklassen, mens avledningsmorfemer endrer ordklassen til et ord. Eksempler
# til bøyningsmorfemer er «spiser», «spiste» og til avledningsmorfemer:
# «huslig», «bryting».

                    ### 3 Strenger i Python ###
# a) Her bruker jeg .read() for å lese tekstfilen.
tekstfil = open("In01.txt", "r")
les = tekstfil.read()

# b)
erTeller = (les.count("er"))
print("Det er nøyaktig ", erTeller, " forekomster av bokstavsekvensen 'er' i \
denne teksten.", sep = "")

# Her bruker jeg først split for å lage en liste av string objekter, og går
# gjennom den ved hjelp av en for-løkke og øker telleren med en for hver eneste
# forekomst av strenger som slutter på "er".
splitter = les.split()
teller = 0
for ord in splitter:
    if ord.endswith("er") == True:
        teller += 1
print("Det er nøyaktig ", teller, " forekomster av ord som slutter på 'er' i \
denne teksten.", sep = "")

# c) Her bruker jeg [-2:] for å slice de to siste indeksene fra splitter listen.
liste = []
for ord in splitter:
    liste.append(ord[-2:])

# Her bruker jeg .join for å konvertere listen til en tekststreng.
print("Her er en streng av endelser: ", " ".join(liste), ".", sep = "")

                    ### 4 Tokenisering ###
# a) Her bruker jeg split igjen men denne bestemmer denne gangen å splitte etter
# hvert eneste linjeskift. Etter det, går jeg gjennom linjene ved hjelp av en
# for-løkke og splitter igjen etter hvert mellomrom. Til slutt går jeg gjennom
# hvert eneste ord og printer ut ordene.
lineSplitter = les.split("\n")
for linje in lineSplitter:
    ord = linje.split()
    for ord in ord:
        print("Ett ord per linje: ", "'", ord, "'", ".", sep = "")

# b) Her bruker jeg den forrige listen splitter som inneholder alle ordene, og
# går deretter gjennom den med en for-løkke for å øke telleren med hvert eneste
# ord som er i lista.
ordTeller = 0
for ord in splitter:
    ordTeller += 1
print("Det er nøyaktig ", ordTeller, " ord i denne teksten.", sep = "")

                    ### 5 Tokenisering av norsk tekst ###
# a) Her åpner jeg en ny fil, men bruker write istedenfor read og bruker den
# samme måten som på 4 a) for å printe ett ord per linje inne i teksten. Til
# slutt bruker jeg "\n" for å skille ordene i den nye teksten med et linjeskift.
nyFil = open("nyfil.txt", "w")
lineSplitter = les.split("\n")
for linje in lineSplitter:
    ord = linje.split()
    for ord in ord:
        skriv = nyFil.write(ord + "\n")

# b) Feilene er nok at ordene som blir skrevet ut inneholder tegnsetting, og
# annet form for symboler. Nettsider blir også skrevet ut som et helt ord, og
# man har også anførselstegn som blir telt som et ord hvis det er et mellomrom
# mellom dem. Til slutt har vi også datoer og tidspunkter, som blir også telt
# som ord.
