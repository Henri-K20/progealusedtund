nimi = ""
vaste = ""
i = 0
loomad = []
knimi = ""
while True:
    nimi = input("Sisestage oma ees- ja perekonnanimi.\n:").title()
    vaste = input("Kas teil on lemmikloomasi? jah/ei\n:").lower()
    if vaste == "jah":
        vaste = input("Kas teil on kass või koer?\n:").lower()
        if vaste == "kass":
            i = int(input("Mitu tükki?\n:"))
            for kass in range(i):
                loomad.append(input(f"Sisestage {kass+1}. kassi nimi.\n:"))
            print(nimi+", olen kindel, et "+" ja ".join([", ".join(loomad[:-1]),loomad[-1]]), "on armsad!")
            break
        elif vaste == "koer":
            vaste = input("Mis liiki on koer?\n:")
            knimi = input("Mis on ka koera nimi?\n:")
            print(f"{nimi}, teil on ilus {vaste} koer, {knimi}.")
            break
    elif vaste == "ei":
        vaste = input("Kas teil on konsoole? jah/ei\n:").lower()
        if vaste == "jah":
            i = int(input("Mitu tükki?\n:"))
            for konsool in range(i):
                knimi = input(f"Sisestage {konsool+1}. konsooli nimi.\n:")
            if i > 1:
                print("go touch grass, nerd")
                break
            elif i <= 1:
                print(f"{nimi}, loodan, et oled oma {knimi} konsooliga epic gamer!")
                break
        elif vaste == "ei":
            print("Head aega!")
            break