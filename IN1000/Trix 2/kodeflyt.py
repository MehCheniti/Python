pris = 50 #1
tekst = input("Skriv inn alder: ") #2
alder = int(tekst) #3

if alder < 12 or alder > 67: #4
    print("Du må betale", pris*0.5, "kr") #5
else:
    print("Du må betale", pris, "kr")
