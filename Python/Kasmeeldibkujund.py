from tkinter import *
age = 0
pikkus = 0
nimi = ""
kujundid = ["ring", "ruut", "kolmnurk", "ovaal"]
meeldib = []
värv = ""
kys = False

while not kys:
    try:
        age = int(input("Kui vana olete?\n:"))*10
        pikkus = int(input("Sentimeetrites, kui pikk olete?\n:"))
        nimi = input("Sisestage oma ees- ja perekonnanimi.\n:").title()ja
    except ValueError:
        input("Sisestuse väärtustüüp on vale! Vajutage enter, et uuesti proovida...")
    else:
        kasmeeldib = input("Kas teile meeldivad geomeetrilised kujundid? jah/ei\n:").lower()
        if kasmeeldib == "ei":
            print("Arusaadav.")
            break
        elif kasmeeldib == "jah":
            kys = True
            raam = Tk()
            raam.title("Lemmikud!")
            tahvel = Canvas(raam, width=1200, height=1200)
            for kujund in kujundid:
                vaste = input(f"Kas teile meeldib {kujund}? jah/ei \n:").lower()
                meeldib.append(vaste)

värv = input("""
######################
Sisestage lemmik värv.

Red
Black
Yellow
Cyan
Blue
Green
Purple
Pink
Orange

######################
:""").lower()

if meeldib[0] == "jah":
    print(meeldib[0])
    tahvel.create_oval(100,100,100+age,100+age, fill=värv)
if meeldib[1] == "jah":
    print(meeldib[1])
    tahvel.create_rectangle(800,100,800+age,100+age, fill=värv)
if meeldib[2] == "jah":
    print(meeldib[2])
    tahvel.create_polygon(1000,800,1000+age,800+age,1000-age,800+age, fill=värv, outline=värv)
if meeldib[3] == "jah":
    print(meeldib[3])
    tahvel.create_oval(200,800,100+age,800+age, fill=värv)
    
tahvel.create_text(600,600,text=f"Palun {nimi} Siin on sinu lemmikkujundid!")

tahvel.pack()
raam.mainloop()
