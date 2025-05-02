fail = open("Andmed\joostud.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 10:
        print(float(rida))