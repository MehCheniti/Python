def skriv_med_trykk(param):
    print (param + "!")

i = 0
while i < 5:
    inn = input("Gi meg et kraftuttrykk! ")
    if (inn.lower() == "nei"):
        break
    skriv_med_trykk(inn)
