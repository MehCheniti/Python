# Oppretter skattekart
skattekart =  []
stoerrelse = 5
for e in range(stoerrelse):
    a = []
    for e in range(stoerrelse):
        a.append("O")
    skattekart.append(a)

# Skriver ut skattekartet foer foerste gjetning
for e in skattekart:
    for f in e:
        print (f, end="")
    print("")

# Lar spiller 1 gjette
print("Spiller 1, du skal gjemme skatten!")
gyldig = False
# Ber om input frem til vi faar gyldige koordinater
while (gyldig != True):
    print("Hvor vil du gjemme skatten?")
    in_x = input("Oppgi x-koordinat: ")
    in_y = input("Oppgi y-koordinat: ")
    if in_y.isdigit() and in_y.isdigit():
        x = int(in_x)
        y = int(in_y)
        if (x < stoerrelse and x > 0 and y < stoerrelse and y > 0):
            skattekart[y][x] = "X"
            gyldig = True
        else:
            print("Ugyldig plassering!")
    else:
        print("Ugyldig input!")

# "Visker ut" skjermen for aa skjule informasjon for spiller 2
for e in range (100):
    print("\n")

# Lar spiller 2 gjette paa plassering
print("Spiller 2, du skal finne skatten!")
antall_gjetninger = 3
funnet_skatt = False
# Lar spiller 2 fortsette aa gjette saa lenge skatten ikke er funnet
# og de har flere forsoek igjen
while(antall_gjetninger > 0 and funnet_skatt == False):
    print("Antall forsoek igjen:", antall_gjetninger)
    gyldig = False
    while (gyldig != True):
        print("Hvor vil du lete etter skatten?")
        in_x = input("Oppgi x-koordinat: ")
        in_y = input("Oppgi y-koordinat: ")
        if in_y.isdigit() and in_y.isdigit():
            x = int(in_x)
            y = int(in_y)
            if (x < stoerrelse and x > 0 and y < stoerrelse and y > 0):
                if skattekart[y][x] == "X":
                    funnet_skatt = True
                    gyldig = True
                else:
                    skattekart[y][x] = "#"
                    gyldig = True
            else:
                print("Ugyldig plassering!")
        else:
            print("Ugyldig input!")
    antall_gjetninger = antall_gjetninger-1

# Gir tilbakemelding til spiller 2
if funnet_skatt:
    print("Gratulerer, du fant skatten!")
else:
    print("Beklager, du fant ikke skatten!")

# Skriver ut skattekartet paa nytt
for e in skattekart:
    for f in e:
        print (f, end="")
    print("")
