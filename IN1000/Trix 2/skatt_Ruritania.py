inntekt = float(input("Inntekt? "))
if inntekt < 10000:
    print("Du betaler: ", inntekt * 0.1)
else:
    print("Du betaler: ", 10000 * 0.1 + (inntekt - 10000) * 0.3)
