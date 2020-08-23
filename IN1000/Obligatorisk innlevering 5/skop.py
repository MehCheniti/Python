# Først defineres funksjonen minFunksjon, som ikke skal ta imot noen parametre.
# Deretter defineres prosedyren hovedprogram, som heller ikke tar noen
# parametre. Deretter kalles hovedprogram. Inne i hovedprogram opprettes en
# variabel a med verdi 42. Deretter oppretter vi en variabel b med verdien 0.
# Så blir variabelen b printet ut. Etter det blir b lik a (42). Også kaller vi
# på minFunksjon. I minFunksjon kjører vi en for-løkke: variabelen c får
# verdien 2, også blir c printet ut. Etter det får c verdien +1 (det vil si 3),
# og b får verdien 10. Men etter dette steget oppstår det en feil i programmet:
# variabelen a er ikke definert i funksjonen minFunksjon. Ingenting blir
# returnert og vi får da en NameError.

def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
