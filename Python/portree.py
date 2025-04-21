from tkinter import *
raam = Tk()
raam.title("Portree!")
tahvel = Canvas(raam,width=300,height=300,background="white")

while True:
    nahk = input("Sisestage oma nahavärv inglise keeles. nt brown või beige, saate ka kasutada hex arve! nt #008000.\n:")
    try:
        pea = int(input("""
########################
Sisestage valiku number:
1. Nokamüts
2. Torumüts
3. Fedora
4. Ei ole mütsi.
:"""))
    except ValueError:
        input("Sisestage arv! Vajutage enterit, et uuesti proovida...")
    else:
        match pea:
            case 1:
                pea = PhotoImage(file="Pildid/nokamüts.png")
                break
            case 2:
                pea = PhotoImage(file="Pildid/torumüts.png")
                break
            case 3:
                pea = PhotoImage(file="Pildid/fedora.png")
                break
            case 4:
                pea = PhotoImage(file="Pildid/juuksed.png")
                break
            case _:
                input("Seda ei ole valikus! Vajutage enterit, et uuesti proovida...")

while True:
    try:
        face = int(input("""
######################
Mis tuju on teil?
1. hea
2. tavaline
3. halb
4. üllatunud
5. tülpinud

Sisestage valiku arv.
:"""))
    except ValueError:
        input("Sisestage arv! Vajutage enterit, et uuesti proovida...")
    else:
        match face:
            case 1:
                face = PhotoImage(file="Pildid/hea.png")
                break
            case 2:
                face = PhotoImage(file="Pildid/tavaline.png")
                break
            case 3:
                face = PhotoImage(file="Pildid/halb.png")
                break
            case 4:
                face = PhotoImage(file="Pildid/üllatunud.png")
                break
            case 5:
                face = PhotoImage(file="Pildid/tülpinud.png")
                break
            case _:
                input("Seda ei ole valikus! Vajutage enterit, et uuesti proovida...")

while True:
    try:
        ilm = int(input("""
######################
Missugune on ilm?
1. Pilvitu
2. pilvine
3. vihmane

Sisestage valiku arv.
:"""))
    except ValueError:
        input("Sisestage arv! Vajutage enterit, et uuesti proovida...")
    else:
        match ilm:
            case 1:
                ilm = tahvel.create_rectangle(0,0,300,300,fill="lightblue",outline="lightblue")
                break
            case 2:
                ilm = tahvel.create_rectangle(0,0,300,300,fill="white",outline="white")
                break
            case 3:
                ilm = tahvel.create_rectangle(0,0,300,300,fill="gray",outline="gray")
                break
            case _:
                input("Seda ei ole valikus! Vajutage enterit, et uuesti proovida...")

base = PhotoImage(file="Pildid/base.png")

try:
    tahvel.create_oval(105,105,195,195,fill=nahk)
except TclError:
    tahvel.create_oval(105,105,195,195,fill="beige")
else:    
    tahvel.create_image(150,150,image=base,anchor=CENTER)
    tahvel.create_image(150,165,image=face,anchor=CENTER)
    tahvel.create_image(150,100,image=pea,anchor=CENTER)

tahvel.pack()
raam.mainloop()