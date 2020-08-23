tall = int(input("Tall, nå. "))

def print_primtall(N):
    teller = N-1
    er_primtall = True

    while teller > 1 :
        if N % teller == 0 :
            er_primtall = False
        teller-=1

    if er_primtall :
        print("Fant primtall ", N)

while tall > 1 :
    print_primtall(tall)
    tall-=1
