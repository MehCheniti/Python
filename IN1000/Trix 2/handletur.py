br = 20
me = 15
os = 40
yo = 12

sum = 0

print("Hei, og velkommen til butikken.")
a = int(input("Hvor mange brød vil du ha? "))
sum+= int(a*br)
b = int(input("Hvor mange melk vil du ha? "))
sum+= int(b*me)
c = int(input("Hvor mange ost vil du ha? "))
sum+= int(c*os)
d = int(input("Hvor mange yoghurt vil du ha? "))
sum+= int(d*yo)
print("Du skal betale", sum, "kroner.")
