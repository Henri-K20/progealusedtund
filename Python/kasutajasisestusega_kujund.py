# kirjuta programm mis
# küsib kasutajalt tsükli sees kui vana ta on (tühja sisestuse puhul küsitakse uuesti niikaua kuni kasutaja on midagi kirjutanud)
# - kui kasutaja on noorem kui 3 aastat, ütle kasutajale et on liiga noor, ning kujundit ei joonistata
# küsib kasutajalt tsükli sees mis on ta lemmikvärv
# - Valikusse pange(punane oranz kollane roheline helesinine tumesinine lilla roosa must valge pruun tumerohline ja teal)
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on
# - kasutajasisend tõlgitakse turtle jaoks inglise keelde ifide abil
# - - kasutaja peab saama öelda vastuse küsimusele (kas sinu lemmikvärv on siin) kas jah või ei, ning kui ei
# - - siis paku kasutajale valida kaks lähimat värvi, ja moodusta hex arvutuse abil neist seguvärv
# küsib kasutajalt tsükli sees mis on ta lemmikkujund
# - Valikusse pange(ring, ruut, võrdhaarne kolmnurk, kuusnurk)
# - kasutajasisend tuleb standardiseerida sõnetöötlusmeetoditega
# - kui kasutaja ei sisesta midagi mis on valikus, töötab tsükkel niikaua kuni kasutaja sisestab midagi mis on
# Põhinedes kasutajalt saadud andmetele, joonista kasutaja lemmikvärviga tema lemmikkujund. Joonistamine ise peab ka tsüklitega toimima
# Siis tagasta konsooli sõnum "Palun <nimi>, siin on sinu <värv> <kujund>!"

vanus = 0
noor = True
värvid = ["punane", "oranz", "kollane", "roheline", "helesinine", "tumesinine", "lilla", "roosa", "must", "valge", "pruun", "tumeroheline", "teal"]
värv = ""
ivärv = ""
ivärvlist = []
kujundid = ["ring", "ruut", "võrdhaarne kolmnurk", "kuusnurk"]
kujund = ""
nimi = ""

while True:

    nimi = str(input("Sisestage oma nimi.\n->"))
    try:
        vanus = int(input("Sisestage oma vanus. \n->"))
    except ValueError:
        print("Andmetüübi sisestuse viga!")
        input("Vajuta enterit, et edasi minna...")
    else:
        if vanus < 3:
            print("Olete liiga noor!")
            break
        else:
            noor = False
            break

while not noor:
    värv = input("""
-------------------------
Mis on teie lemmik värv?
Punane
Oranz
Kollane
Roheline
Helesinine
Tumesinine
Lilla
Roosa
Must
Valge
Pruun
Tumeroheline
Teal

Kui teie lemmik värv puudub, siis sisestage Q.
-------------------------
->""").lower()
    if värv == "q":
        värv = input("""
----------MIXER----------
Sisestage esimene lähim värv.
Punane
Oranz
Kollane
Roheline
Helesinine
Tumesinine
Lilla
Roosa
Must
Valge
Pruun
Tumeroheline
Teal
-------------------------
->""").lower()
        if värv == "punane":
            värv1 = "FF 00 00"
        elif värv == "oranz":
            värv1 = "FF A5 00"
        elif värv == "kollane":
            värv1 = "FF FF 00"
        elif värv == "roheline":
            värv1 = "00 80 00"
        elif värv == "lightblue":
            värv1 = "AD D8 E6"
        elif värv == "tumesinine":
            värv1 = "00 00 8B"
        elif värv == "lilla":
            värv1 = "80 00 80"
        elif värv == "roosa":
            värv1 = "FF C0 CB"
        elif värv == "must":
            värv1 = "00 00 00"
        elif värv == "valge":
            värv1 = "FF FF FF"
        elif värv == "pruun":
            värv1 = "96 4B 00"
        elif värv == "tumeroheline":
            värv1 = "00 64 00"
            
        värv = input("""
----------MIXER----------
Sisestage teine lähim värv.
Punane
Oranz
Kollane
Roheline
Helesinine
Tumesinine
Lilla
Roosa
Must
Valge
Pruun
Tumeroheline
Teal
-------------------------
->""").lower()
        if värv == "punane":
            värv2 = "FF 00 00"
        elif värv == "oranz":
            värv2 = "FF A5 00"
        elif värv == "kollane":
            värv2 = "FF FF 00"
        elif värv == "roheline":
            värv2 = "00 80 00"
        elif värv == "lightblue":
            värv2 = "AD D8 E6"
        elif värv == "tumesinine":
            värv2 = "00 00 8B"
        elif värv == "lilla":
            värv2 = "80 00 80"
        elif värv == "roosa":
            värv2 = "FF C0 CB"
        elif värv == "must":
            värv2 = "00 00 00"
        elif värv == "valge":
            värv2 = "FF FF FF"
        elif värv == "pruun":
            värv2 = "96 4B 00"
        elif värv == "tumeroheline":
            värv2 = "00 64 00"
        värvlist1 = värv1.split()
        värvlist2 = värv2.split()
        ivärvlist.append(hex(int(round((int(värvlist1[0],16) + int(värvlist2[0],16))/2))))
        ivärvlist.append(hex(int(round((int(värvlist1[1],16) + int(värvlist2[1],16))/2))))
        ivärvlist.append(hex(int(round((int(värvlist1[2],16) + int(värvlist2[2],16))/2))))
        i = 3
        while i != 0:
            ivärvlist[i-1] = ivärvlist[i-1][2:]
            i -=1
        ivärv = "#"+"".join(ivärvlist)
        print(ivärv)
        break
    elif not värv in värvid:
        input("Seda värvi ei leidu! Vajuta enterit, et edasi minna...")
    else:
        if värv == "punane":
            ivärv = "red"
        elif värv == "oranz":
            ivärv = "orange"
        elif värv == "kollane":
            ivärv = "yellow"
        elif värv == "roheline":
            ivärv = "green"
        elif värv == "helesinine":
            ivärv = "lightblue"
        elif värv == "tumesinine":
            ivärv = "darkblue"
        elif värv == "lilla":
            ivärv = "purple"
        elif värv == "roosa":
            ivärv = "pink"
        elif värv == "must":
            ivärv = "black"
        elif värv == "valge":
            ivärv = "white"
        elif värv == "pruun":
            ivärv = "brown"
        elif värv == "tumeroheline":
            ivärv = "darkgreen"
        break
while ivärv != "":
    kujund = input("""
-------------------------
Mis on teie lemmikkujund?
Ring
Ruut
Võrdhaarne kolmnurk
Kuusnurk
-------------------------
->""").lower()
    if not kujund in kujundid:
        input("Seda kujundit ei ole valikus! Vajuta enterit, et edasi minna...")
    else:
        break

while kujund != "":
    from turtle import *
    
    color(ivärv)
    begin_fill()
    if kujund == "ring":
        circle(vanus*3.14)
    elif kujund == "ruut":
        for i in range(4):
            fd(100)
            lt(90)
    elif kujund == "võrdhaarne kolmnurk":
        for i in range(3):
            fd(200)
            lt(120)
    elif kujund == "kuusnurk":
        for i in range(6):
            fd(200)
            lt(60)
    end_fill()
    print(f"Palun {nimi}, siin on teie {värv} {kujund}!")
    exitonclick()
    break
