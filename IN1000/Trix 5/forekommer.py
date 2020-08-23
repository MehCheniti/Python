def forekommer(tekst, tegn):
    for c in tekst:
        if c == tegn:
            return True
        else:
            return false

def uten_repetisjon(tekstsreng):
    nytekst = ""
    for i in range(len(tekststreng))
        if not forekommer(tekst[0:i], tekst[1]):
            nytekst += tekst[i]
        return nytekst

def antall_forskjellige(tekst):
    return len(uten_repetisjon(tekst))
