# NB! kõik küsimised on tsüklis mis kontrollitud tsüklimuutujaga (mitte True ja break)
# NB! kõik sisendud töödeldakse standardkujule
# NB! kõik funktsionaalsed osad mis pole üldise programmi osa, peab olema kirjutatud funktsioonina
# kasutab tkinterit
# kirjuta programm mis
#
# Küsib kasutajalt tema ees ja perekonnanime
# küsib kasutajalt tema sünnipäeva
# küsib kasutajalt tema vanust
# küsib kasutajalt mida ta oma sünnipäevakaardile näha tahab
# - kas õhupalle (jah/ei) #õhupalli joonistamine on alamfunktsioon
# - - kui jah siis mitu (arv)
# - kas kooki küünaldega (jah/ei) (küünalde arv on kasutaja vanus +=1) #koogi ja küünalde joonistamine on alamfunktsioon)
# - kas kingitust õnnesoovidega (palju õnne vanus +=1 saamise puhul)
# - või kas kõike korraga
# programm joonistab kasutajale tkinteri abil sünnipäevakaardi.

from tkinter import *
raam = Tk()
raam.title("Palju Õnne!")
tahvel = Canvas(raam,height=500,width=500)

def õhupall(kogus):
    x = 0
    y = 0
    for i in range(kogus):
        if i != 0 and i % 10 == 0:
            y+= 65
            x = 0
        tahvel.create_polygon(33+x,96+y,34+x,69+y,46+x,55+y,58+x,55+y,73+x,62+y,74+x,92+y,54+x,107+y,61+x,117+y,48+x,117+y,54+x,107+y,fill="red",outline="black")
        x += 45
def kookKüünlad():
    x = 0
    y = 0
    z = 0
    for i in range(vanus+1):
        if i != 0 and i % 21 == 0:
            y+= 20
            z+= 3
            x = z
        tahvel.create_polygon(90+x,455,90+x,260+y,94+x,260+y,94+x,250+y,94+x,260+y,100+x,260+y,100+x,455,fill="white",outline="black")
        tahvel.create_polygon(93+x,257+y,91+x,254+y,93+x,250+y,94+x,247+y,96+x,250+y,97+x,252+y,97+x,255+y,95+x,257+y,fill="yellow",outline="black")
        x += 15
    tahvel.create_rectangle(80,356,410,470,fill="beige")
    tahvel.create_oval(80,356,410,356,fill="black")
    tahvel.create_oval(80,470,410,470,fill="black")



nimi = ""
sünna = ""
vanus = ""
vaste = ""
kogus = 0

while nimi == "" or sünna == "" or vanus == "":
    nimi = input("Sisestage oma ees ja perekonnanimi!\n:").capitalize()
    sünna = input("Sisestage oma sünnipäev.\n:")
    try:
        vanus = int(input("Sisestage vanus.\n:"))
    except ValueError:
        input("Väär sisend! Vajutage enterit, et uuesti proovida.")
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
                kookKüünlad()
            case 2:
                #õnnesoov
                pass
            case 3:
                #kõik korraga
                pass
            case _:
                input("Seda ei ole valikus! Vajutage enterit, et uuesti proovida.")

õhupall(kogus)


tahvel.create_text(250,39,text=f"Palju õnne {nimi}! Sündisid {sünna}, oled nüüd {vanus+1}. aasta vanune!")
tahvel.pack()
raam.mainloop()