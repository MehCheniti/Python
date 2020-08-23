#Dette programmet fungerer som et system som beregner billettpris avhengig av
#brukerens alder.

def prosedyre():
    alder = int(input("Hvor gammel er du? "))

    billettpris = 0

    if alder <= 17:
        billettpris = 30
    elif alder >= 63:
        billettpris = 35
    else:
        billettpris = 50

#Her bruker jeg sep="" for å kunne ha mellomrom.
    print("Du må betale ", billettpris, " kroner.", sep="")

prosedyre()
prosedyre()
prosedyre()
prosedyre()

#Problemet med denne prosedyren er at oppgaven ber oss om å skrive en if-test
# som sjekker om brukeren er over 17 år gammel før vi får vite at vi også skal
# sjekke om brukeren er 63 år eller eldre.
