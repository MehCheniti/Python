from gjest import Gjest
from rorbu import Rorbu

def hovedprogram():
    rorbua = Rorbu()

    gjest = Gjest()
    teller = 100
    while teller != 0:
        rorbua.nyGjest(gjest)
        teller -= 1

    rorbua.fortellVits(200)

    print(rorbua.hvorMorsomtHarViDet())

    rorbua.fortellVits(1000)

    print(rorbua.hvorMorsomtHarViDet())

hovedprogram()
