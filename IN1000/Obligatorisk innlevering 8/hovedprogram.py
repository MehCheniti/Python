from node import Node
from rack import Rack
from regneklynge import Regneklynge

def main():

    abel = Regneklynge(12)

    teller = 650
    while teller != 0:
            abel.settInnNode(Node(64, 1))
            teller -= 1

    teller = 16
    while teller != 0:
            abel.settInnNode(Node(1024, 2))
            teller -= 1

    print("Noder med minst 32 GB: ", abel.noderMedNokMinne(32), ".", sep = "")
    print("Noder med minst 64 GB: ", abel.noderMedNokMinne(64), ".", sep = "")
    print("Noder med minst 128 GB: ", abel.noderMedNokMinne(128), ".", sep = "")

    print("")

    print("Antal prosessorer: ", abel.antProsessorer(), ".", sep = "")
    print("Antal racks: ", abel.antRacks(), ".", sep = "")

main()
