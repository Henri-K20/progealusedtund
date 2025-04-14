from time import *
from tkinter import *
from keyboard import *

raam = Tk()
raam.title("WOW!")
tahvel = Canvas(raam,width=600,height=600)
px = 0
py = 0


pall = tahvel.create_oval(275,275,325,325,fill="black")
#sein = tahvel.create_rectangle(0,0,100,600,fill="black")


def update():
    raam.update()
    tahvel.pack()

def up():
    tahvel.move(pall,0,-5)
    raam.after(5)

def down():
    tahvel.move(pall,0,5)
    raam.after(5)
    
def left():
    tahvel.move(pall,-5,0)
    raam.after(5)

def right():
    tahvel.move(pall,5,0)
    raam.after(5)

while True:
    if is_pressed("q"):
        quit()
    if is_pressed("w"):
        up()
    if is_pressed("s"):
        down()
    if is_pressed("a"):
       left()
    if is_pressed("d"):
        right()
    if px >= 100:
        tahvel.move(pall,px+5,py)










    print(f"x: {px} , y: {py}")
    update()
raam.mainloop()






