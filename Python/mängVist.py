from tkinter import *
from keyboard import *
raam = Tk()
raam.title("Mäng!")
tahvel = Canvas(raam,width=500,height=500,background="white")
border = tahvel.create_rectangle(100,100,400,400)
pall = tahvel.create_rectangle(225,225,275,275,fill="limegreen")

def update():
    tahvel.pack()
    raam.update()

def move():
    pallcoord = tahvel.coords(pall)
    bordercoord = tahvel.coords(border)
    print(f"Sein:{bordercoord}\n Box:{pallcoord}")
    x = 0
    y = 0
    
    if bordercoord[0] > pallcoord[0]:
        x=5
    elif is_pressed("a"):
        x-=5
    if bordercoord[2] < pallcoord[2]:
        x=-5
    elif is_pressed("d"):
        x+=5
    if bordercoord[1] > pallcoord[1]:
        y=5
    elif is_pressed("w"):
        y-=5
    if bordercoord[3] < pallcoord[3]:
        y=-5
    elif is_pressed("s"):
        y+=5
    
    tahvel.move(pall,x,y)
    tahvel.after(1)
    update()

while True:
    if is_pressed("q"):
        break
    move()
raam.mainloop()