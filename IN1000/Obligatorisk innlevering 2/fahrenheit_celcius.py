# Dette programmet spør brukeren om å angi temperatur i farenheit og skriver
# det ut, for å så konvertere det til celcius og skriver det ut også.

#Her bruker jeg en stor bokstav F for å skille ut ordene "temp" og "Fahr" på
#variabelen.
tempFahr = int(input("Tast inn temperatur i fahrenheit: "))

print("Temperatur i fahrenheit: ", tempFahr, " °F.", sep="")

tempCel = ((tempFahr) - 32) * 5 / 9

#Her bruker jeg round(x,2) for å få resultatet til å vise kun 2 desimaltall.
print("Temperatur i celcius: ", round(tempCel, 2), " °C.", sep="")
