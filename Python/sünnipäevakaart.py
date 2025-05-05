from tkinter import *
raam = Tk()
raam.title("Palju Õnne!")
tahvel = Canvas(raam,height=500,width=500)

def õhupall(kogus):
    tahvel.create_polygon(349,55,365,45,384,57,383,76,370,90,375,97,366,97,370,90,353,79,fill=)










nimi = ""
sünna = ""
vanus = ""
vaste = ""
kogus = 0

while nimi == "" or sünna == "" or vanus == "":
    nimi = input("Sisestage oma ees ja perekonnanimi!\n:").capitalize()
    sünna = input("Sisestage oma sünnipäev.\n:").lower()
    vanus = input("Sisestage vanus.\n:").lower()

while vaste == "":
    try:
        vaste = int(input("""
####################################
Mida soovite sünnipäevakaardil näha?
0. õhupalle
1. kooki küünlatega
2. õnnesoove
3. kõike korraga
####################################
:"""))
    except ValueError:
        input("Väär sisend! Vajutage enterit, et uuesti proovida.")
    else:
        match vaste:
            case 0:
                while kogus == 0:
                    try:
                        kogus = int(input("Sisestage, mitu õhupalli soovite!\n:"))
                    except ValueError:
                        input("Väär sisend! Vajutage enterit, et uuesti proovida.")
            case 1:
                #kook + küünlad
                pass
            case 2:
                #õnnesoov
                pass
            case 3:
                #kõik korraga
                pass
            case _:
                input("Seda ei ole valikus! Vajutage enterit, et uuesti proovida.")




tahvel.create_text(250,39,text=f"Palju õnne {nimi}! Sündisid {sünna}, oled nüüd {vanus+1}. aasta vanune!")
tahvel.pack()
raam.mainloop()