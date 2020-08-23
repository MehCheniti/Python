tall = []
while len(tall) <= 5:
  heltall1 = int(input("Første? "))
  tall.append(heltall1)
  heltall2 = int(input("Andre? "))
  tall.append(heltall2)
  heltall3 = int(input("Tredje? "))
  tall.append(heltall3)
  heltall4 = int(input("Fjerde? "))
  tall.append(heltall4)
  heltall5 = int(input("Femte? "))
  tall.append(heltall5)

for e in tall:
  print(int(heltall1) + int(heltall2) + int(heltall3) + int(heltall4) + int(heltall5))

teller = 0
print("Tall under 10:")
while teller < len(tall) :
    if tall[teller] < 10 :
        print(tall[teller])
    teller+=1

finnes_fem = False
teller = 0
while teller < len(tall) :
    if tall[teller] == 5 :
        finnes_fem = True
    teller+=1
if finnes_fem :
    print("Fem finnes i listen")
else:
    print("Fem finnes ikke i listen")
