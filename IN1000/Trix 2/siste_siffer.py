a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a % 10 == b % 10:
    print("a og b har like siste siffer")
if a % 10 == c % 10:
    print("a og c har like siste siffer")
if b % 10 == c % 10:
    print("b og c har like siste siffer")
