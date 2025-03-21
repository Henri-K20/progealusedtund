nimi = ""
pknimi = ""

snimi = ""
spknimi = ""
summa = 0
ksumma = 0

kood = 0
jääk = 1424
kood1 = 0
kood2 = 0

while nimi != "Siim":
    nimi = input("Sisestage nimi.\n:").capitalize()
while pknimi != "Kallas":
    pknimi = input("Sisestake perekonnanimi.\n:").capitalize()

while True:
    try:
        kood = str(input("Sisestage kood.\n:"))
    except ValueError:
        input("Väär andmetüüp, vajutage enterit et edasi minna...")
    else:
        if kood == "0000" or kood == "1234":
            print("0000 ja 1234 ei sobi, on liiga lihtsad.")
        else:
            break
while True:
    tegevus = input("""
------------------------------------
Kas te soovite:

1. Vaadata konto jääki
2. Vaadata seifis oleva kulla kogust
3. Teha tehingut
------------------------------------
:""")
    if tegevus == "1":
        input(f"Teil on kontol €{jääk}. Vajutage enter, et edasi minna...")
        break
    elif tegevus == "2":
        try:
            kood2 = int(input("Sisestage teine parool!\n:"))
        except ValueError:
            input("Väär andmetüüp, vajutage enterit et edasi minna...")
        else:
            if kood2 == 0000 or kood2 == 1234:
                print("0000 ja 1234 ei sobi.")
            else:
                print("""
 _________
/__\_24K__\
""" * jääk)
                input(f"Teil on {jääk} kullakangi. Vajutage enter, et edasi minna...")
    elif tegevus == "3":
        while kood1 != 1234 and kood2 != 4321:
            try:
                kood1 = int(input("Sisestage esimene kood.\n:"))
                kood2 = int(input("Sisestage teine kood.\n:"))
            except ValueError:
                input("Väär andmetüüp, vajutage enterit et edasi minna...")
            else:
                break
        break
    else:
        input("See ei ole valikus, vajutage enterit et edasi minna...")

while kood1 == 1234 and kood2 == 4321:
    tegevus = input("""
-----------TEHINGUMENÜÜ-------------
1. Ülekanne
2. Välju
------------------------------------
:""")
    if tegevus == "1":
        try:
            snimi = input("Sisestage saaja eesnimi.\n:").capitalize()
            spknimi = input("Sisestage saaja perekonnanimi.\n:").capitalize()
            summa = int(input("Palju raha soovite saata?\n:"))
            ksumma = int(input("Mitu kullakangi soovite saata?\n:"))
        except ValueError:
            input("Väär andmetüüp, vajutage enterit et edasi minna...")
        else:
            print(f"""
--------Saadetis-on-Teel------------
Saaja nimi:
{snimi}

Saaja perekonnanimi:
{spknimi}

Summa:
€{summa}

Kulla kogus:
{ksumma}
------------------------------------
""")
            break
    elif tegevus == "2":
        print(f"Headaega {nimi} {pknimi}, järgmise korrani, teie kuld on ohutult hoiul meie juures.")
        break
    else:
        input("See ei ole valikus, vajutage enterit et edasi minna...")