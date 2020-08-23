from person import Person

def hovedprogram():
    meg = Person("Mehdi", "ingen")
    enAnnen = Person("Angelina Jolie", "ingen")

    meg.minStatus()

    meg.bryllup(enAnnen)
    enAnnen.bryllup(meg)

    meg.minStatus()

hovedprogram()
