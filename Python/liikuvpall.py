from time import *
from tkinter import *
from keyboard import *

raam = Tk()
raam.title("WOW!")
tahvel = Canvas(raam,width=600,height=600)
px = 0
py = 0
pall = tahvel.create_oval(275,275,325,325,fill="black")

while not is_pressed("q"):
    if is_pressed("w"):
        tahvel.move(pall,px,py-5)
        tahvel.pack()
        raam.update()
        raam.after(5)
        
    if is_pressed("s"):
        tahvel.move(pall,px,py+5)
        tahvel.pack()
        raam.update()
        raam.after(5)

    if is_pressed("a"):
        tahvel.move(pall,px-5,py)
        tahvel.pack()
        raam.update()
        raam.after(5)
        
    if is_pressed("a"):
        tahvel.move(pall,px+5,py)
        tahvel.pack()
        raam.update()
        raam.after(5)

tahvel.pack()
raam.mainloop()






