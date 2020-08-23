sum = 30

stasjon1 = input("Første stasjon! Hvor mange går på bussen? ")
a = sum-int(stasjon1)
if a <= 0:
    print("Bussen er full.")

stasjon2 = input("Andre stasjon! Hvor mange går på bussen? ")
b = a-int(stasjon2)
if b <=0:
    print("Bussen er full.")

stasjon3 = input("Tredje stasjon! Hvor mange går på bussen? ")
c = b-int(stasjon3)
if c <=0:
    print("Bussen er full.")
