x = [0]
y = [1]


c = 0
d = 0
swap = 0

# Sorterer listen x
while c < len(x) :
    while d < len(x) - c - 1 :
        if x[d] > x[d+1] :
            swap = x[d]
            x[d] = x[d+1]
            x[d+1] = swap
        d+=1
    d = 0
    c+=1

c = 0

# Sorterer listen y
while c < len(y) :
    while d < len(y) - c - 1 :
        if y[d] > y[d+1] :
            swap = y[d]
            y[d] = y[d+1]
            y[d+1] = swap
        d+=1
    d = 0
    c+=1

# Utskrifter
print("Hjørner:")
print("Nede venstre:\t[", x[0], ",", y[0], "]")
print("Nede høyre:\t["  , x[len(x)-1], ",", y[0], "]")
print("Øvre høyre:\t["  , x[len(x)-1], ",", y[len(y)-1], "]")
print("Øvre venstre:\t[", x[0], ",", y[len(y)-1], "]")
