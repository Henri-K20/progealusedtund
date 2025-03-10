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

if input("Kas te ehitate maja? jah/ei"+"\n:").lower() == "jah":
    while True:
        
        vastus = input("""
######################
Kas teil on midagi puudu?
- Seinamaterjal
- Vundamendimaterjal
- Katusematerjal
- Põrandamaterjal
- Mööbel

Kui ei, siis vajutage enterit.
######################
:""").lower()
        pindala = input("Kui suur on ehitatav pindala? m2"+"\n:")
        if vastus == "seinamaterjal":
            materjal = input("""
######################
Valige materjal:
Tellis - 1 eur/m2
Puit - 2 eur/m2
Betoon - 2.5 eur/m2
######################
:""").lower()
        
        elif vastus == "vundamendimaterjal":
            materjal = input("""
######################
Valige materjal:
Paekivi - 1 eur/m2
Betoon - 2.5 eur/m2
######################
:""").lower()
        
        elif vastus == "katusematerjal":
            materjal = input("""
######################
Valige materjal:
Plekk - 2 eur/m2
Eterniit - 1.5 eur/m2
Tõrvapapp - 3 eur/m2
######################
:""").lower()
        
        elif vastus == "põrandamaterjal":
            materjal = input("""
######################
Valige materjal:
Puitlaud - 2 eur/m2
Parkett - 1.25 eur*m2
Linoleum - 3.2 eur/m2
######################
:""").lower()
        elif vastus == "mööbel":
            materjal = input("""
######################
Valige materjal:
Köögimööbel - 50 eur/tk
Elutoamööbel - 35 eur/tk
Vannitoa sisustus - 65 eur/tk
Magamistoa mööbel - 100 eur/tk
######################
:""").lower()
        
print("Head päeva!")