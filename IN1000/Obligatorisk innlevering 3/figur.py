# Oppgave 5: Tegn en figur
# Filnavn: figur.py
# 1. Lag en tom liste, velg navnet selv.
# 2. Lag to variabler (bredde og lengde) som tar imot koordinater fra bruker.
# 3. Legg disse variablene inn i den tomme lista.
# 4. Bruk koordinatene fra lista til å tegne et figur med EzGraphics.

# Dette programmet ber brukeren om å skrive inn bredde og lengde for å så
# tegne en rektangel eller et kvadrat.

koordinater = []

bredde = int(input("Skriv inn bredde: "))
lengde = int(input("Skriv inn lengde: "))

koordinater.append(bredde)
koordinater.append(lengde)

from ezgraphics import GraphicsWindow
win = GraphicsWindow()
win.setTitle("Et Figur")
canvas = win.canvas()
canvas.drawRectangle(100, 150, koordinater[0], koordinater[1])
win.wait()
