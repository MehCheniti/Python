from student import Student

ordliste = {}

mehdi = Student("Mehdi", "Meh", "976 19 804")
cheniti = Student("Cheniti", "Che", "408 91 679")
mc = Student("MC", "M", "804 19 976")

ordliste["Mehdi"] = mehdi
ordliste["Cheniti"] = cheniti
ordliste["MC"] = mc

for key, value in ordliste.items():
    value.printInfo()

def sjekkStudent():
    inp = input("Hvilken student vil du søke etter? ")
    for keys, values in ordliste.items():
        if inp == keys:
            values.printInfo()
        else:
            print(inp, " finnes ikke i systemet.", sep = "")

sjekkStudent()
