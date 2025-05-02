fail = open("Andmed\laulusõnad.txt", encoding="UTF-8")
sõnad = []
kokku = 0
vaste = ""

for rida in fail:
    sõnad.append(rida.strip())
    kokku += rida.count("a") + rida.count("e") + rida.count("i") + rida.count("o") + rida.count("u") + rida.count("õ") + rida.count("ä") + rida.count("ö") + rida.count("ü") + rida.count("y")
fail.close()

print("Laulusõnad on:\n", *sõnad, sep="\n")
print(f"\nTäishäälikuid on: {kokku}")
print(f"\nSõnad, mis on pikemad kui 7 tähte on:")

for rida in sõnad:
    for sõna in rida.split():
        if len(sõna) > 7:
            print(sõna)
for i in range(4):
    sõnad.append(input(f"\nSisesta uus rida ({i+1})\n:"))

while vaste != "ei" and vaste != "jah":
    vaste = input("\nKas soovite näha sõnu uuesti? jah/ei\n:").lower()
    if vaste == "ei":
        print("Arusaadav.")
    elif vaste == "jah":
        print(*sõnad,sep="\n")
    else:
        input("Väär sisestus! Vajutage enter, et uuesti proovida...")