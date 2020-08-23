hey = open("tall.txt", "r")
tall = []
linje = hey.readline()
while linje != "":
    tall.append(int(linje))
    linje = hey.readline()

def antall_forekomster(liste, heltall):
    ant = 0
    for i in tall:
        if i == heltall:
            ant += 1
        return ant

def flest_forekomster(liste):
    flest_forekomster = liste[0]
    antall_forekomster = 0
    for verdi1 in liste:
        teller = 0
        for verdi2 in liste:
            if verdi1 == verdi2:
                teller += 1
        if (teller > antall_forekomster):
            flest_forekomster = verdi1
            antall_forekomster = teller
    return flest_forekomster

print ("Tallet 34 forekommer", antall_forekomster(tall, 34), "ganger.")
print ("Det er flest forekomster av tallet", flest_forekomster(tall))
