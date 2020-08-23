# Dette programmet spør deg om du vil ha en brus og svarer tilsvarende
brus = input('Vil du kjøpe en brus? ') #Først bruker jeg input for å spørre om brukeren vil ha en brus eller ikke.
print(brus)

if brus == 'ja': #Her bruker jeg if for å skrive ut noe om brukeren svarer ja.
    print('Her har du en brus!')
elif brus == 'nei': #Her bruker jeg elif for å skrive ut noe om brukeren svarer nei.
    print('Den er grei.')
else: #Hvis brukeren svarer med noe annet enn ja eller nei så bruker jeg else for å skrive ut noe gjensidig.
    print('Det forstod jeg ikke helt.')
