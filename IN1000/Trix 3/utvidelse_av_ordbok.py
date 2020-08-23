ordbok = {"melk" : 14.90, "brod" : 24.90, "yoghurt" : 12.90, "pizza" : 39.90}
print(ordbok)

while len(ordbok) < 5:
    vare0 = input("Tast inn en vare: ")
    pris0 = float(input("Tast inn prisen: "))
    ordbok[vare0] = pris0

vare1 = 0
while vare1 != "A":
    vare1 = input("Tast inn en vare (tast inn A for å avslutte): ")
    pris1 = float(input("Tast inn prisen: "))
    ordbok[vare1] = pris1
print(ordbok)
