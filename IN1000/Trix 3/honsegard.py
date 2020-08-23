høner = int(input("Hvor mange høner? "))
reven = str(input("Kommer reven? "))
bonden = str(input("Sover bonden? "))

if reven == "ja" and bonden == "ja":
    print(høner - 1, " høner.", sep="")
elif reven == "ja" and bonden == "nei":
    print(høner, " høner, free 190 kr.", sep="")
elif reven == "nei":
    print("Nothing interesting happens.")
