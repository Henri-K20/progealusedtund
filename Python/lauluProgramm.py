fail = open("Andmed/laulusõnad.txt")
sõnad = []

for sõna in fail:
    sõnad.append(sõna)
print(sõnad)
fail.close()