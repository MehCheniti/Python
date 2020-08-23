# Dette programmet regner ut gjennomsnittet av flere gjennomsnittstemperaturer.

#Her bruker jeg .rstrip() for å fjerne alle \n'ene.
fil = open("temperatur.txt", "r")
liste = []
for i in fil:
    liste.append(i.rstrip())

#Her deler jeg alle elementene (kallt i) i listen på lengden av listen for å få
#gjennomsnittet.
def gjennomsnitt(liste2):
    summ = 0
    for i in liste2:
        summ += float(i) / len(liste2)
    return summ

print("Gjennomsnittet av temperaturene er ", gjennomsnitt(liste), " ºC.",
sep="")
