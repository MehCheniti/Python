from gjest import Gjest
from rorbu import Rorbu

def hovedprogram():
    førsteEpisode = Rorbu()
    andreEpisode = Rorbu()

    førsteEpisode = andreEpisode

    gjest = Gjest()
    for gjester in range(50):
        førsteEpisode.nyGjest(gjest)
    for gjester in range(75):
        andreEpisode.nyGjest(gjest)

    print(førsteEpisode.hentAntallGjester())

    førsteEpisode.fortellVits(10000)
    print(førsteEpisode.hvorMorsomtHarViDet())

hovedprogram()
