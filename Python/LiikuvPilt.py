from tkinter import *
from math import *

raam = Tk()
raam.title("spinning...")
tahvel = Canvas(raam,width=800,height=800)
r = 200
nurk = 40
i = 0

while True:
    try:
        img = int(input("""
    #######################
    Valige lemmik objekt:

    1. Pall
    2. Ruubiku-Kuubik
    3. Vihmavari
    4. Vape

    Sisestage valiku arv.
    :"""))
    except ValueError:
        input("Väär sisend! Vajutage enter, et uuesti proovida...")
    else:
        if img > 4 or img < 1:
            input("Seda pole valikus! Vajutage enter, et uuesti proovida...")
        else:
            break

match img:
    case 1:
        img = PhotoImage(file="Pildid/Pall.png")

    case 2:
        img = PhotoImage(file="Pildid/kuubik.png")

    case 3:
        img = PhotoImage(file="Pildid/vihmavari.png")

    case 4:
        img = PhotoImage(file="Pildid/vape.png")

objekt = tahvel.create_image(400,400,image=img)

while True:
    x = ((r/2*pi)*cos(i/nurk))
    y = ((r/2*pi)*sin(i/nurk))
    i += 1
    tahvel.coords(objekt, x, y)
    print(f"x:{x}, y:{y}")
    tahvel.move(objekt,400,400)
    raam.after(1)
    tahvel.pack()
    raam.update()

raam.mainloop()