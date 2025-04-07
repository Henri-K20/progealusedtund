nimi = ""
pknimi = ""
idkood = 0
while nimi == "" and pknimi == "":
    nimi = input("Sisestage oma eesnimi. \n:")
    pknimi = input("Sisestage oma perekonnanimi. \n:")
    fnimi = (nimi +" "+ pknimi).title()

while True:
    idkood = input(fnimi+", palun sisestage oma isikukood. (Sisestage ei kui soovite lahkuda.) \n:").lower()
    if idkood == "ei":
        print("Näeme järgmine kord.")
        break
    else:
        try:
            idkood = int(idkood)
        except ValueError:
            input("Väär sisestus, isikukoodis on ainult numbrid! Vajutage enter, et uuesti proovida.")
        else:
            if len(str(idkood)) == 11:
                print("Aitäh")
                break
            else:
                print("Isikukood peab olema 11 arvumärki pikk!")