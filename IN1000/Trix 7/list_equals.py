def equals(liste_en, liste_to):
    teller = 0
    like = True

    if len(liste_en) != len(liste_to):
        like = False
    while teller < len(liste_en):
        if liste_en[teller] != liste_to[teller]:
            like = False
        teller += 1

    if like:
        print("De har samme elementer i samme rekkefølge.")
    else:
        print("De har ikke samme elementer i samme rekkefølge.")

liste1 = [6, 2, 3]
liste2 = [6, 2, 3]

equals(liste1, liste2)
