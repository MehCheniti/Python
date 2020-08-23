liste = [6, -4, 7, -2, 8, -3, 9, -11]

minst = liste[0]
for i in liste:
    if i < minst:
        minst = i
print(i)

størst = liste[0]
for i in range(1, len(liste)):
    if liste[i] > størst:
        størst = liste[i]
print(størst)
