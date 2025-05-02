fail = open("Andmed\joostud.txt")
kokku = 0
for rida in fail:
    if float(rida) > 10:
        kokku+= float(rida)
print(f"Te olete kokku jooksnud: {kokku} kilomeetrit.")