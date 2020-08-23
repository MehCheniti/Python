# Dette er ikke en lovlig kode, siden vi forsøker å slå sammen et heltall, som
# er variabelen b, med tekstrengen "Hei!".

# En av problemene man kan møte når man kjører denne koden er en error av type
# "TypeError". En annen mulig problem kan være om man limer inn koden uten å
# sette inn et innrykk etter den tredje linjen, som vil føre til en
# "IndentationError".

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
