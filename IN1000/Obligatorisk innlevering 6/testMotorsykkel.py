from motorsykkel import Motorsykkel

def hovedprogram():

    motorsykkel1 = Motorsykkel("Yamaha", 10020017, 170)
    motorsykkel2 = Motorsykkel("Honda", 11221001, 150)
    motorsykkel3 = Motorsykkel("Ducati", 10012211, 180)

    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt()

    motorsykkel3.kjor(10)

    print("Nye kilometerstand for Ducati: ", motorsykkel3.hentKilometerstand(),
    ".", sep="")

hovedprogram()
