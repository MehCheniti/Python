ordbok = {}

ordbok.update({"Arne": 22334455, "Lisa": 95959595, "Jonas": 97959795, "Peder":
12345678})

navn = str(input("Tast inn et navn: "))
if navn in ordbok:
    nummer = ordbok[navn]
    print("Nummer til ", navn, " er ", nummer, ".", sep="")
else:
    print("I AM ERROR")
