from random import randint

eludeArv = 3
kullaTykk = 0
raha = 5
haldjaidAidanud = 0
mängläbi = False
vastusPolitseile = ""

while (eludeArv > 0) or (mängläbi == False):
    
    #sündmus 1
    print("Astusid redeli alt läbi, ning nägid ", end="")
    juhtum = randint(1,3)
    
    if juhtum == 1:
        print("musta kassi.")
        eludeArv -= 1
        print("Su süda tegi suure jõnksu ja tundus nagu sa oleks kaotanud terve ühe elu.")
    
    elif juhtum == 2:
        print("maas mingisuguse tabletikese. Sellel on peal pikachu pilt.")
        seejuhtum = randint(1,2)
        if seejuhtum == 1:
            print("Otsustasid seda süüa, oli väga hea, aga kahjuks kaotasid kõik elud!")
            eludeArv = 0
        else:
            print("Maast üles võttes, lagunes tablett tolmuks. Pühkisid käed ja liikusid edasi.")
    else:
        print("et sinu auto juures seisab politseinik. \n Nägu on tal üsna punane, ning selgelt näost näha põlevat viha.")
        print("Politseinik ütleb:")
        while True:
            vastusPolitseile = input("Teie auto on pargitud kõnniteele liiga lähedale! Kas liigutate oma autot?\n:").lower()
            if vastusPolitseile == "jah":
                print("Viisid oma auto teise kohta, leidsid autost välja tulles maast ühe eurose.")
                raha += 1
                break
            elif vastusPolitseile == "ei":
                print("Politseinik teeb teile trahvi.")
                raha -= 20
                break
            else:
                print("ah? ei saa aru...")
    print(f"""
------------------------
Sinu hetkeseis on:
Elusid = {eludeArv}
Raha = {raha}
Kullakange = {kullaTykk}
------------------------
""")
    input("Vajuta enter, et jätkata\n:")
    if eludeArv == 0:
        print("Mäng läbi!")
        mängläbi = True
        break
    
    #sündmus 2
    print("Kõndisid tänaval edasi ja nägid veidrat objekti. ")
    juhtum = randint(1,3)
    
    if juhtum == 1:
        print(" see nägi välja nagu pisike lendav taldrik.")
        print("Sa vaadatsid seda natuke, kui järsku muutus käeshoitav lendav taldrik kullakangiks.")
        print("Said ühe kulla kangi!")
        kullaTykk += 1

    elif juhtum == 2:
        print("Lähemale minnes, arvastasid, et keegi on hambaharja sõlme keeranud.")
        seejuhtum = randint(1,2)
        if seejuhtum == 1:
            print("Sa ei teadnud mida teha, otsustasid seda nuusutada.")
            print("Kohutav lehk võttis sult ühe elu.")
            eludeArv -= 1
        else:
            print("Otsustasid visata selle sõiduteele, parasjahu sõitis teel Elon Musk, ja\nta isejuhtiv auto ei osanud midagi teha, sõitis üle ja keeras auto vastu seina.\nElon suri.")
            print("Leitsid ta rahakotist 5 raha. Ta oli vaene ront.")
            raha += 5
            
    else:
        if kullaTykk > 19:
            print("Kasutaja ette ilmus haldjas. Haldjas ütles: 'meil on abi vaja!'")
            while True:
                vastusPolitseile = input("'Me kasutame kullakange inimeste vähi ravimiseks, kas loovutad 5 kullakangi?'")
                if vastusPolitseile == "jah":
                    print("Otsustasid haldjaid aidata, kaotasid 5 kullakangi, aga said terve kuhja head tuju.")
                    kullaTykk -= 5
                    haldjaidAidanud += 1
                    if haldjaidAidanud == 3:
                        print("'Oled meid palju aidanud, tule meile külla, kohtleme sind kui kangelast.'")
                        print("Oled võitnud, mäng läbi.")
                        mängläbi = True
                        break
                elif vastusPolitseile == "ei":
                    print("Selge, kuni järgmise korrani.")
                    break
                else:
                    print("ah? ei saa aru...")
            
            
            
        else:
            print("See oli musta värvi lapik ristkülik.")
            print("Ees kõnnib mees, kes ilmselgelt pillas oma rahakoti maha.")
            while True:
                vastusPolitseile = input("Kas tagastad rahakoti mehele?\n:").lower()
                if vastusPolitseile == "jah":
                    print("Otsustasid rahakoti tagastada, mees tänas ja andis suure kullakangi.")
                    kullaTykk += 1
                    break
                elif vastusPolitseile == "ei":
                    print("Rahakotis oli 10 raha.")
                    raha += 10
                    break
                else:
                    print("ah? ei saa aru...")
    print(f"""
------------------------
Sinu hetkeseis on:
Elusid = {eludeArv}
Raha = {raha}
Kullakange = {kullaTykk}
------------------------
""")
    input("Vajuta enter, et jätkata\n:")
    if eludeArv == 0:
        print("Mäng läbi!")
        mängläbi = True
        break
    
    #sündmus 3 pood
    print("Jõudes poodi, nägid midagi huvitavat.")
    juhtum = randint(1,3)
    
    if juhtum == 1:
        while True:
            vastusPolitseile = input("See oli allahindlus viineripirukatel. Kas ostad neid?").lower()
            if vastusPolitseile == "jah":
                print("Sööd nendest kõhu täis. Saad ühe elu juurde!")
                eludeArv += 1
                raha -= 2
                break
            elif vastusPolitseile == "ei":
                print("Leiad vähe kallimad, lihapirukad ja ostad need. Need maksavad rohkem, seega ei saa nii palju võtta.\nEi saa kõhtu täis.")
                raha -= 5
                break
            else:
                print("ah? ei saa aru...")

    elif juhtum == 2:
        print("See oli su vana sõber.\nSa pole teda kaua näinud, ta andis sulle 10 raha.")
        raha += 10
    else:
        while True:
            vastusPolitseile = input("See oli rott! Kas lööd maha?")
            if vastusPolitseile == "jah":
                print("Lõid roti maha ja leidsid ta seest 5 kullatükki! Kahjuks, võitluses kaotasid 1 elu...")
                kullaTykk += 5
                eludeArv -= 1
                break
            elif vastusPolitseile == "ei":
                print("Rott vaatab sinu poole ja jookseb minema, kuuled kaugemalt inimeste kiljeid...")
                break
            else:
                print("ah? ei saa aru...")
            
    print(f"""
------------------------
Sinu hetkeseis on:
Elusid = {eludeArv}
Raha = {raha}
Kullakange = {kullaTykk}
------------------------
""")
    input("Vajuta enter, et jätkata\n:")
    if eludeArv == 0:
        print("Mäng läbi!")
        mängläbi = True
        break
        