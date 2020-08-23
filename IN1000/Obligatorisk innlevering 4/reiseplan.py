# Dette programmet ber brukeren om å taste inn 5 reisemål, klesplagg og
# avreisedatoer for å så skrive ut en liste som innholder det brukeren skrev
# inn. Deretter ber det brukeren om å oppgi et nummer, og skriver da ut et
# element av listen avhengig av nummeret som ble tastet inn.

#Her bruker jeg .append() for å legge til elementer i listene.
steder = []
for i in range(5):
    innlest1 = str(input("Vennligst tast inn et reisemål: "))
    steder.append(innlest1)

klesplagg = []
for i in range(5):
    innlest2 = str(input("Vennligst tast inn et klesplagg: "))
    klesplagg.append(innlest2)

avreisedatoer = []
for i in range(5):
    innlest3 = str(input("Vennligst tast inn en avreisedato: "))
    avreisedatoer.append(innlest3)

#Her bruker jeg .append() for å legge til lister til listen.
reiseplan = []
reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

for i in range(1):
    print(reiseplan)

#Her bruker jeg list[input] for å gi verdien til i1 og i2 indeksen av listen (
#som brukeren har tastet inn).
innlest4 = int(input("Vennligst oppgi en plass i reiseplanen (0 - 2): "))
i1 = reiseplan[innlest4]
print(i1)

innlest5 = int(input("Vennligst oppgi en plass i valgte kategori (0 - 4): "))
i2 = i1[innlest5]
print(i2)

#Her bruker jeg if og and for å ha alle verdiene mellom 0 - 2 og 0 - 4.
if 0 <= innlest4 <= 2 and 0 <= innlest5 <= 4:
    print(i1, i2)
else:
    print("Ugyldig input!")
