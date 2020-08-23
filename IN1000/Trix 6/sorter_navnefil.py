navn = open("navn2.txt", "r")
personer = []
hunder = []

for linje in navn:
    if linje[0] == "P":
        personer.append(linje.rstrip())
    elif linje[0] == "H":
        hunder.append(linje.rstrip())

print(personer)
print(hunder)
