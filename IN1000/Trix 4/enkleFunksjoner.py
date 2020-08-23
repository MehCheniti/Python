def velkommen(bruker):
    print("Velkommen ", bruker, ".", sep="")
velkommen(input("Brukernavn? "))

def strenginator(streng1, streng2):
    return(str(streng1) + " " + str(streng2))
strengA = "Mehdi"
strengB = "Cheniti."
konkatenert = strenginator(strengA, strengB)
print(konkatenert)
