# Oppgave 5: Beslutninger II
# Filnavn: quiz.py
# 1. Skriv et program der du ber brukeren om å svare på fem forskjellige quiz
# spørsmål som du velger selv. Svarer brukeren riktig skal han få
# tilbakemeldingen "Riktig!", svarer brukeren feil skal han få tilbakemeldingen
# "Feil svar!".

# Dette programmet stiller spørsmål til brukeren og gir tilbakemelding på om
# svarene er riktig eller feil.

#Her bruker jeg .lower() for å få programmet til å godta svaret med både små og
#store bokstaver.
svar1 = input("Hva er hovedstaden til Bolivia? ")
if svar1.lower() == "sucre":
    print("Riktig!")
else:
    print("Feil svar!")

svar2 = input("Hvilket år fikk Norge sin egen grunnlov? ")
if svar2 == "1814":
    print("Riktig!")
else:
    print("Feil svar!")

svar3 = input("Nevn den syvende planeten i solsystemet. ")
if svar3.lower() == "uranus":
    print("Riktig!")
else:
    print("Feil svar!")

svar4 = input("For å lage bronse trenger man kobber og... ")
if svar4.lower() == "tin":
    print("Riktig!")
else:
    print("Feil svar!")

svar5 = input("Hvilket år skjedde den første bemannede månelanding? ")
if svar5.lower() == "1969":
    print("Riktig!")
else:
    print("Feil svar!")
