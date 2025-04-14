from tkinter import *
raam = Tk()
raam.title("")
tahvel = Canvas(raam, width = 1000, height = 1000)

kogus = 0
pin = 0
ikood = 0
i = 0

def raha():
    tahvel.create_rectangle(200,400,800,600,fill="green")
    tahvel.create_text(500,500,text=kogus, font=("Arial", 64, "bold"))

def kaart():
    tahvel.create_rectangle(200,300,800,700, fill="orange")
    tahvel.create_text(500,500,text=ikood, font=("Arial", 64, "bold"))

def frown():
    tahvel.create_oval(400,400,600,600,fill="beige",outline="black")
    tahvel.create_oval(430,430,500,500,fill="white")
    tahvel.create_oval(510,430,580,500,fill="white")
    tahvel.create_oval(445,445,480,480,fill="black")
    tahvel.create_oval(525,445,560,480,fill="black")
    tahvel.create_line(450,550,475,525,525,525,550,550,fill="black",width=4)
    tahvel.create_line(450,350,450,650,width=2)
    tahvel.create_line(550,350,550,650,width=2)
    tahvel.create_line(475,350,475,650,width=2)
    tahvel.create_line(500,350,500,650,width=2)
    tahvel.create_line(575,350,575,650,width=2)
    tahvel.create_line(525,350,525,650,width=2)
    tahvel.create_line(425,350,425,650,width=2)
    tahvel.create_line(400,350,400,650,width=2)
    tahvel.create_line(600,350,600,650,width=2)
    
    
while True:
    try:
        pin = int(input("Sisestage pin\n:"))
        ikood = int(input("Sisestage isikukood\n:"))
    except ValueError:
        input("Väär andmetüüp! Vajutage enter, et uuesti proovida...")
    else:
        if (pin == 1234 and len(str(ikood)) == 11) or (i >= 2):
            break
        else:
            print("Vale pin ja/või isikukoodi pikkus!")
            i += 1

if i >= 2:
    frown()
if pin == 1234:
    while True:
        try:
            tahab = int(input("""
###########################
Kas soovite:
1. Raha välja võtta
2. Pangakaarti tagasi saada

Sisestage valiku nr.
###########################
:"""))
        except ValueError:
            input("Väär andmetüüp! Vajutage enter, et uuesti proovida...")
        else:
            if tahab == 1:
                kogus = int(input("Palju soovite välja võtta?\n:"))
                raha()
            elif tahab == 2:
                kaart()
            break
tahvel.pack()
raam.mainloop()