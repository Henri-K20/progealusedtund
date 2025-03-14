# kirjuta programm mis küsib kasutajalt kas ta ehitab maja.
# - kui jah, siis küsi kas tal on olemas:
# - - Seinamaterjal, vundamendimaterjal, katusematerjal, põrandamaterjal, mööbel
# - kui tal midagi puudub, siis:
# - - küsi kui suur on ehitatav ala (seinakogupindala, põrandakogupindala jms)
# - - paku erinevat materjali ehitatava ala ehituseks:
# - - - katuse jaoks (plekk, eterniit, tõrvapapp - igalühel on oma hind)
# - - - seinade jaoks (tellis, puit, betoon - igalühel on oma hind)
# - - - vundamendi jaoks (paekivi, betoon - igalühel on oma hind)
# - - - põranda jaoks (puitlaud, parkett, linoleum - igalühel on oma hind)
# - isegi kui kasutajal on majaehituse jaoks kõik olemas, paku talle sisustust
# - variandid - köögimööbel, elutoa mööbel, vannitoa sisustus, magamistoa mööbel
# - Kui kasutaja ostab midagi, küsi kas tal on kliendikaart olemas, kui on, küsi talt kliendikaardi numbrit (123456)
# - Kliendikaardi olemasolul saab ostult -15% alla mööblilt, -20% alla ehitusmaterjalilt.
# Väljasta kasutajale Kviitung kõigest mida ta ostis.

hinnad = [[1, 2, 2.5], [1, 2.5], [2, 1.5, 3], [2, 1.25, 3.2], [50, 35, 65, 100]]

materjal = ""
vastus = ""
summa = 0


while True:
    ehitab = input("Kas te ehitate maja? jah/ei"+"\n:")
    if ehitab == "ei" or ehitab == "":
        print("Head päeva!")
        break
    elif ehitab.lower() != "jah" or ehitab == "ei":
        print("Väär sisend!")
    elif ehitab.lower() == "jah":
        while True:
            
            vastus = input("""
#########################
Kas teil on midagi puudu? valige nr
0. Seinamaterjal
1. Vundamendimaterjal
2. Katusematerjal
3. Põrandamaterjal

Kui ei, siis vajutage enterit.
#########################
:""").lower()

            if vastus == "":
                break
            
            pindala = float(input("Kui suur on ehitatav pindala? m2"+"\n:"))
            if vastus == "0":
                materjal = int(input("""
######################
Sisestage valiku nr:
0. Tellis - 1 eur/m2
1. Puit - 2 eur/m2
2. Betoon - 2.5 eur/m2
######################
:""").lower())
        
            elif vastus == "1":
                materjal = int(input("""
######################
Sisestage valiku nr:
0. Paekivi - 1 eur/m2
1. Betoon - 2.5 eur/m2
######################
:""").lower())
        
            elif vastus == "2":
                materjal = int(input("""
######################
Sisestage valiku nr:
0. Plekk - 2 eur/m2
1. Eterniit - 1.5 eur/m2
2. Tõrvapapp - 3 eur/m2
######################
:""").lower())
        
            elif vastus == "3":
                materjal = int(input("""
######################
Sisestage valiku nr:
0. Puitlaud - 2 eur/m2
1. Parkett - 1.25 eur/m2
2. Linoleum - 3.2 eur/m2
######################
:""").lower())

            summa += (pindala * hinnad[int(vastus)][int(materjal)])
            print(f"Hetkene summa on teil: {summa}")
    break






if materjal != "":
    while True:
        mööbelvaste = input("Kas ei soovi äkki mööblit? jah/ei" + "\n:")
        if mööbelvaste.lower() == "jah":
            vastus = 4
            materjal = input("""
######################
Sisestage valiku nr:
0. Köögimööbel - 50 eur/tk
1. Elutoamööbel - 35 eur/tk
2. Vannitoa sisustus - 65 eur/tk
3. Magamistoa mööbel - 100 eur/tk
######################
:""").lower()
            summa += hinnad[int(vastus)][int(materjal)]
            break
        elif mööbelvaste.lower() == "ei":
            break
        else:
            print("Väär sisend!")

    print(f"Maksumus kokku on: €{summa}")




