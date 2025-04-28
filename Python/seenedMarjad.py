seened = ["lisa juurde", "pilvik", "kukeseen", "mürklid", "puravik", "võiseen"]
seenedSisu = [
            "Pilvikute viljakehad on lihakad, kübara ja keskse jalaga, keskmised kuni suured.",
            "Kukeseene viljakeha värv ulatub kollasest oranžini, see on lihakas ja sageli lehtrikujuline.",
            "Mürkli viljakeha kübar on pigem habras ja iseloomulikult munajalt koonusjas.",
            "Puravike viljakehad on lihakad, kübar ja jalg selgelt välja arenenud, torukeste kiht eraldub kübarast kergesti, tihti leidub loor.",
            "Võiseene kübar on 8–24 cm laiune, lame, keskkohast nõgus, ooker-, kuld- või sidrunikollane, selgelt vöödiline, takerkarvane kleepuv-limane."]

marjad = ["lisa juurde", "mustikas", "jõhvikas", "vaarikas", "karusmari", "must sõstar"]
marjadSisu = [
            "Taime eestikeelne nimetus 'mustikas' viitab tema marjade värvile, samuti sellele, et küpsed marjad purunevad kergesti ning määrivad käsi ja nägu.",
            "Jõhvikas kasvab rabas, ja kasvab maadligi. Tema juured on väga lühikesed, kuna rabas on väga paks turbakiht, mis ei lase taime juurtel põhjaveeni pääseda. Jõhvikal on väikesed lehed.",
            "Vaarika varred on enamasti ogalised ja seest suure säsiga. Varre eluiga kestab kaks aastat. Teisel aastal vars viljub ja siis kuivab.",
            "Karusmari (rahvapärase nimetusega tikker) õitseb aprillis-mais. Õied on rippuvad, rohekad või punakad, ühe-kahe kaupa lühivõrsetel lehtede kaenlas. Marjad on rohelised, kollakad, punakad või purpurjad, kerajad, munajad või piklikud, paljad või karvased.",
            "Must sõstar on tumeda koorega mari, mis on rikkalik C-vitamiini poolest. Seda kasutatakse sageli moosides, mahlades ja tervislikes jookides."]

tahabLugeda= True

while tahabLugeda:
    midaOtsib = ""
    valik = ""
    while midaOtsib == "":
        midaOtsib = input("Kas te otsite seent või marja?\n->").lower()
        if midaOtsib != "seent" and midaOtsib != "marja":
            midaOtsib = ""
            input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")

    if midaOtsib == "seent":
         while valik not in seened: 
            print("########################## \n#Sisestage valiku number.#")
            for index, seen in enumerate(seened):
                print(f"#{index}: {seen.capitalize()}"+(22-(len(seen)+len(str(index))))*" "+"#")
            print("##########################")
            try:
                valik = seened[int(input("\n->"))]
            except (IndexError, ValueError):
                input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")
            else:
                if seened.index(valik) == 0:
                    seened.append(input("Sisestage uue seene nimi.\n->").lower())
                    seenedSisu.append(input(f"Sisestage uue seene tekst.\n->").capitalize())
                else:
                    print(seenedSisu[seened.index(valik)-1])

    elif midaOtsib == "marja":
        while valik not in marjad: 
            print("########################## \n#Sisestage valiku number.#")
            for index, mari in enumerate(marjad):
                print(f"#{index}: {mari.capitalize()}"+(22-(len(mari)+len(str(index))))*" "+"#")
            print("##########################")
            try:
                valik = marjad[int(input("\n->"))]
            except (IndexError, ValueError):
                input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")
            else:
                if marjad.index(valik) == 0:
                    marjad.append(input("Sisestage uue marja nimi.\n->").lower())
                    marjadSisu.append(input(f"Sisestage uue marja tekst.\n->").capitalize())
                else:
                    print(marjadSisu[marjad.index(valik)-1])

    while valik != "jah" and valik != "ei":
        valik = input("\nKas soovite lõpetada? jah/ei\n->").lower()
        if valik == "jah":
            tahabLugeda = False
        elif valik == "ei":
            tahabLugeda = True
        else:
            input("Väär sisestus! Vajuta enterit, et uuesti proovida!\n->")