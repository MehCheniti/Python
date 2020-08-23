from person2 import Person
from personsystem import Personsystem

def hovedprogram():

    personsystem = Personsystem()
    personsystem.leggTilPerson(Person("Mehdi"))
    personsystem.leggTilPerson(Person("M"))
    personsystem.leggTilPerson(Person("E"))
    personsystem.leggTilPerson(Person("H"))
    personsystem.leggTilPerson(Person("Cheniti"))
    print(personsystem.finnPerson("Mehdi"), " finnes.", sep="")

    assert personsystem.finnPerson("Mehdi") != None

hovedprogram()
